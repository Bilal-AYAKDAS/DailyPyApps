import requests
import xml.etree.ElementTree as ET
import pandas as pd

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
          "AppleWebKit/537.36 (KHTML, like Gecko)"
          "Chrome/130.0.0.0 Safari/537.36"
          }

URL ="https://www.tcmb.gov.tr/kurlar/today.xml"

def fetch(session):
    """
    Fetches the content from the specified URL using the provided session.

    :param session: The session object to be used for making the HTTP request.
    :type session: requests.Session
    :return: The text content of the response.
    :rtype: str
    :raises HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = session.get(URL,headers=HEADERS)
    response.raise_for_status()
    print(f"Request returned with status code {response.status_code}")
    return response.text


def parse_float_number(value:str):
    """
    Converts a float number represented as a string from using a dot as the decimal separator to using a comma.

    Args:
        value (str): The string representation of the float number.

    Returns:
        str: The modified string with a comma as the decimal separator, or an empty string if the input is None.
    """
    if value is not None:
        return value.replace(".",",")
    else:
        return ""


def xml_parse(xml_data):
    """
    Parses XML data containing currency information and converts it to a CSV file.

    Args:
        xml_data (str): A string containing XML data with currency information.

    Returns:
        None: The function saves the parsed data to a CSV file named 'currency_data.csv'.

    The function performs the following steps:
    1. Parses the XML data to extract currency information.
    2. Converts the extracted data into a list of dictionaries.
    3. Creates a pandas DataFrame from the list of dictionaries.
    4. Saves the DataFrame to a CSV file named 'currency_data.csv' with specified formatting.
    """
    doviz_json = []
    root = ET.fromstring(xml_data)
    for currency in root.findall('Currency'):
        row = {
        "Unit": currency.find('Unit').text ,
        "Isim": currency.find('Isim').text,
        "CurrencyName": currency.find('CurrencyName').text,
        "ForexBuying": parse_float_number(currency.find('ForexBuying').text),
        "ForexSelling": parse_float_number(currency.find('ForexSelling').text),
        "BanknoteBuying": parse_float_number(currency.find('BanknoteBuying').text),
        "BanknoteSelling": parse_float_number(currency.find('BanknoteSelling').text),
        "CrossRateUSD": parse_float_number(currency.find('CrossRateUSD').text),
        "CrossRateOther": parse_float_number(currency.find('CrossRateOther').text),
        }
        doviz_json.append(row)
        df = pd.DataFrame(doviz_json)
        print(df)
        csv_file_path = "currency_data.csv"
        df.to_csv(csv_file_path, index=False, sep=";", encoding="utf-8-sig",float_format="%.4f")



def main():
    """
    Main function to execute the currency tracking script.

    This function creates a requests session, fetches the data using the fetch function,
    and then parses the XML result using the xml_parse function.
    """
    with requests.Session() as session:
        result = fetch(session)
        xml_parse(result)
        

if __name__ =="__main__":
    main()