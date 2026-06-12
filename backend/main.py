from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data import get_stock_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods = ["GET"],
    allow_headers = ["*"]
)

@app.get("/api/stock/{symbol}")
def get_ventas(symbol: str = "AAPL", period: str = "3mo"):
    return get_stock_data(symbol, period)
