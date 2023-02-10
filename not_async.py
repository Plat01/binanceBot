import requests


def get_price(symbol: str) -> float:
    """
    :param symbol: ticker of futures
    :return: current price of futures
    """
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": symbol}
    response = requests.get(url, params=params).json()
    return float(response["price"])


def get_max_price(symbol: str, interval: str) -> float:
    """
    :param symbol: ticker of futures
    :param interval: time interval
    :return: maximum price
    """
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": 1
    }
    response = requests.get(url, params=params).json()
    return float(response[0][2])


if __name__ == '__main__':
    while True:
        price = get_price("XRPUSDT")
        max_price = get_max_price("XRPUSDT", "1h")
        change = max_price - price
        print(change)
        if change > max_price / 100:
            print("Price dropped more then 1 %")

