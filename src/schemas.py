from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import TIMESTAMP


class Ticker(BaseModel):
    id: UUID
    ticker: str
    price: float | int
    ticker_time: float

    class Config:
        from_attributes = True


class TickerAdd(BaseModel):
    ticker: str
    price: float | int
    ticker_time: float


class ModelCurrency(str, Enum):
    btc = "btc"
    eth = "eth"