import aiohttp
import asyncio
import sqlite3
import time


async def get_index_price(session, ticker):
    url = f""
    async with session.get(url) as response:
        data = await response.json()
        return data["result"]["index_price"]