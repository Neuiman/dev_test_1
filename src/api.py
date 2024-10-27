from datetime import datetime

from fastapi import FastAPI


app = FastAPI()


@app.get("/all_data")
async def get_all_data(ticker: str):
    pass


@app.get("/last_price")
async def get_last_price(ticker: str):
    pass


@app.get("/price_by_data")
async def get_price_by_data(ticker: str,
                            first_data: datetime,
                            last_data: datetime) :
    pass



