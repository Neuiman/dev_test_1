from abc import ABC, abstractmethod
from datetime import datetime

from sqlalchemy import insert, select

from src.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def  add_one(self):
        raise NotImplementedError

    async def  get_all_data(self):
        raise NotImplementedError

    async def  get_data_by_date(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):

    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            result = await session.execute(stmt)
            return result.scalar_one()

    async def get_all_data(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    async def get_data_by_date(self, first_date: datetime, last_date: datetime):
        async with async_session_maker() as session:
            stmt = select(self.model).where(first_date < self.model.date < last_date)
            result = await session.execute(stmt)
            result = [row[0].to_read_model() for row in result.all()]
            return result



