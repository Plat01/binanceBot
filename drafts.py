import requests

root_url = "https://api.binance.com/api/v1/klines"
symbol = "XRPUSDT"
interval = "1h"
# root_url = 'https://api.binance.com/api/v1/klines'
# url = root_url + '?symbol=' + symbol + '&interval=' + interval
# response = requests.post("https://api.binance.com/api/v1/klines?symbol=XRPUSDT&interval=1h")
params = {
        "symbol": symbol,
        "interval": interval,
        "limit": 1
    }
print(requests.get("https://api.binance.com/api/v1/klines", params=params).json())
print(requests.get('https://api.binance.com/api/v3/klines?symbol=XRPUSDT&interval=1h&limit=1').json())