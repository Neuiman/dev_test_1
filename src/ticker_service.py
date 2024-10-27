from datetime import datetime

from sqlalchemy.dialects.mssql import TIMESTAMP

from models import Ticker
from repository import AbstractRepository
from schemas import TickerAdd
import uuid


class TickerService:
    def __init__(self, ticker_repository: AbstractRepository):
        self.ticker_repository: AbstractRepository = ticker_repository()

    async def add_ticker(self, ticker: TickerAdd) -> uuid.UUID:
        ticker_dict = ticker.model_dump()
        ticker_id = await self.ticker_repository.add_one(ticker_dict)
        return ticker_id


    async def get_all_tickers(self, ticker):
        all_ticker_data = await self.ticker_repository.get_all_data(ticker)
        return all_ticker_data


    async def get_tickers_by_date(self, ticker, first_date: datetime, last_date: datetime):
        first_date = first_date.timestamp()
        last_date = last_date.timestamp()
        tickers_by_date = await self.ticker_repository.get_data_by_date(ticker, first_date, last_date)
        return tickers_by_date


    async def get_last_ticker_price(self, ticker: str):
        last_ticker_price = await self.ticker_repository.last_ticker_price(ticker)
        return last_ticker_price

