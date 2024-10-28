import ssl

import aiohttp
import asyncio
import time
from aiohttp import ClientSession
import certifi
from database import async_session_maker
from repository import TickerRepository
from schemas import TickerAdd
from ticker_service import TickerService


class DeribitClient:
    def __init__(self, ticker):
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        self.ticker = ticker


    async def make_ticker_object(self):
        url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={self.ticker}_usd"

        async with ClientSession() as session:
            async with session.get(url, ssl=self.ssl_context) as response:
                data = await response.json()

        ticker_object = TickerAdd(ticker=self.ticker, price= data['result']['index_price'], ticker_time=time.time())
        await self.save_ticker(ticker_object)


    @staticmethod
    async def save_ticker(ticker_object):
        await TickerService(TickerRepository).add_ticker(ticker=ticker_object)


# Основная функция для выполнения задачи
async def main():
        while True:
            btc_client = DeribitClient("btc")
            await btc_client.make_ticker_object()
            eth_client = DeribitClient("eth")
            await eth_client.make_ticker_object()

            await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())