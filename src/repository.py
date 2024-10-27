from abc import ABC, abstractmethod
from datetime import datetime

from sqlalchemy import insert, select, and_, TIMESTAMP
from uuid import UUID
from database import async_session_maker
from models import Ticker


class AbstractRepository(ABC):
    @abstractmethod
    async def  add_one(self):
        raise NotImplementedError


    async def  get_all_data(self):
        raise NotImplementedError


    async def  get_data_by_date(self):
        raise NotImplementedError


    async def last_ticker_price(self):
        raise NotImplementedError


class TickerRepository(AbstractRepository):

    model = Ticker

    async def add_one(self, data: dict) -> UUID:
        async with async_session_maker() as session:
            ticker = Ticker(**data)
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()


    async def get_all_data(self, ticker: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(ticker == self.model.ticker)
            result = await session.execute(stmt)
            result = [row[0] for row in result.all()]
            return result


    async def get_data_by_date(self, ticker: str, first_date: float, last_date: float):
        async with async_session_maker() as session:
            stmt = select(self.model).where(and_(first_date < self.model.ticker_time, self.model.ticker_time < last_date, ticker == self.model.ticker))
            result = await session.execute(stmt)
            result = [row[0] for row in result.all()]
            return result


    async def last_ticker_price(self, ticker: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.ticker == ticker).order_by(self.model.ticker_time.desc()).limit(1)
            result = await session.execute(stmt)
            result = [row[0] for row in result.all()]
            return result



