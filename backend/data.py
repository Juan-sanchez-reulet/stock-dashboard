import yfinance as yf
import pandas as pd

def get_stock_data(symbol: str = "AAPL", period: str = "3mo") -> list:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)
    if df.empty:
        return []
    df = df.reset_index()
    df = df[["Date", "Close", "Volume"]]

    # Media móvil de 20 días — promedio de los últimos 20 cierres
    # Los primeros 19 valores serán NaN porque no hay suficientes datos previos
    df["MA20"] = df["Close"].rolling(window=20).mean().round(2)

    df["Date"] = df["Date"].dt.strftime("%d %b %Y")
    df["Close"] = df["Close"].round(2)

    df = df.rename(columns={
        "Date": "fecha",
        "Close": "precio",
        "Volume": "volumen",
        "MA20": "ma20"
    })


    records = df.to_dict("records")
    return [
        {k: (None if isinstance(v, float) and pd.isna(v) else v) for k, v in row.items()}
        for row in records
    ]