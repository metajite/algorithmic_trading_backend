import yfinance as yf

def fetch_historical_prices(market='SP500'):
    ticker = "^GSPC" if market == 'SP500' else market
    data = yf.download(ticker, period="5y")
    return data
