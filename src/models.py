import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import UUID
import uuid

from database import async_session_maker

Base = declarative_base()


class Ticker(Base):
    __tablename__ = "Ticker"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    ticker: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=True)
    ticker_time: Mapped[float] = mapped_column(nullable=True)






