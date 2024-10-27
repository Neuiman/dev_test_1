from pydantic import BaseModel


class Ticker(BaseModel):
    id: int
    ticker: str
    price: float | int
    time: int


class TickerInput(BaseModel):
    ticker: int
    price: float | int
    time: int
