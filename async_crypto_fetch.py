import aiohttp
import asyncio

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
          "AppleWebKit/537.36 (KHTML, like Gecko)"
          "Chrome/130.0.0.0 Safari/537.36"
          }


URLS =["https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=SHIBUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=TONUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=TRXUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT",
       "https://api.binance.com/api/v3/ticker/price?symbol=ETHBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=BTCBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=SOLBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=SHIBBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=ADABNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=TONBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=TRXBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=DOGEBNB",
       "https://api.binance.com/api/v3/ticker/price?symbol=XRPBNB"
       ]

async def fetch(session,url):
    async with session.get(url,headers=HEADERS) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session,url) for url in URLS]
        results =  await asyncio.gather(*tasks)
        for result in results:
            print(result)

if __name__ =="__main__":
    asyncio.run(main())
