import asyncio
import aiohttp


async def get_price(symbol: str) -> float:
    """
    :param symbol: ticker of futures
    :return: current price of futures
    """
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "XRPUSDT"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            return float(data["price"])


async def get_max_price(symbol: str, interval: str) -> float:
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
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            return float(data[0][2])


async def main():
    while True:
        price = await get_price("XRPUSDT")
        max_price = await get_max_price("XRPUSDT", "1h")
        change = max_price - price
        print(change)
        if change > max_price / 100:
            print("Price dropped more then 1 %")

asyncio.run(main())
