from datetime import datetime

from fastapi import FastAPI

from repository import TickerRepository
from schemas import TickerAdd, ModelCurrency
from ticker_service import TickerService


app = FastAPI()


@app.get("/all_data")
async def get_all_data(ticker: ModelCurrency):
    ticker_id = await TickerService(TickerRepository).get_all_tickers(ticker=ticker)
    return ticker_id



@app.get("/last_price")
async def get_last_price(ticker: ModelCurrency):
    ticker_dict = await TickerService(TickerRepository).get_last_ticker_price(ticker=ticker)
    return ticker_dict



@app.get("/price_by_data")
async def get_price_by_data(ticker: ModelCurrency,
                            first_date: datetime,
                            last_date: datetime) :
    ticker_dict = await TickerService(TickerRepository).get_tickers_by_date(ticker=ticker,
                                                                            first_date=first_date,
                                                                            last_date=last_date)
    return ticker_dict



