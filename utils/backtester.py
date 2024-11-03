import pandas as pd

def run_backtest(data):
    # Basic strategy: Buy and hold for 2 days, then evaluate results
    data['Return'] = data['Adj Close'].pct_change()
    cumulative_return = (data['Return'] + 1).cumprod()

    # Simple logic for a 2-day holding period
    data['Signal'] = data['Adj Close'].shift(-2) > data['Adj Close']
    total_trades = data['Signal'].sum()

    results = {
        'total_trades': total_trades,
        'cumulative_return': cumulative_return.iloc[-1],
        'data_points': data.to_dict(orient='records')
    }
    return results
