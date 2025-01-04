# DailyPyApps

**DailyPyApps** is a Python repository containing two powerful tools for retrieving financial data:

1. **TCMB Tracker**: Fetches daily exchange rates from the **Türkiye Cumhuriyet Merkez Bankası (TCMB)** and saves them in a CSV file.
2. **Async Crypto Fetch**: Fetches real-time cryptocurrency prices asynchronously from the **Binance API**.

Both tools are designed to be efficient, user-friendly, and reliable for financial data tracking and analysis.

---

## Features

### TCMB Tracker
- Retrieves daily exchange rate data directly from the TCMB website.
- Parses the XML data to extract key currency information.
- Saves the data in a CSV file for analysis or record-keeping.

### Async Crypto Fetch
- Fetches real-time cryptocurrency prices from Binance.
- Uses asynchronous programming for fast and efficient data retrieval.
- Supports multiple cryptocurrency pairs.

---

## Requirements

Before running the tools, ensure you have the following dependencies installed:

- Python 3.12 
- Required Python libraries:
  - `requests`
  - `aiohttp`
  - `pandas`

Install the dependencies using `pip`:

```bash
pip install requests pandas aiohttp
