import aiohttp
import asyncio
import time

from aiohttp import ClientSession

from database import async_session_maker
from repository import TickerRepository
from schemas import TickerAdd
from ticker_service import TickerService
import requests



async def get_price(ticker):
    url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={ticker}_usd"

    with requests.request('GET', url) as response:
        data = response.json()
        return data['result']['index_price']


# Основная функция для выполнения задачи
async def main():
        while True:

            btc_ticker = TickerAdd(ticker="btc", price=await get_price('btc'), ticker_time=time.time())
            eth_ticker = TickerAdd(ticker="eth", price=await get_price('eth'), ticker_time=time.time())

            async with async_session_maker() as db_session:
                await TickerService(TickerRepository).add_ticker(ticker=btc_ticker)
                await TickerService(TickerRepository).add_ticker(ticker=eth_ticker)

            await asyncio.sleep(60)

# Запуск основной функции
if __name__ == "__main__":
    asyncio.run(main())