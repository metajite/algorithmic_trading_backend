from flask import Flask, request, jsonify
from utils.data_fetcher import fetch_historical_prices
from utils.backtester import run_backtest

app = Flask(__name__)

@app.route('/backtest', methods=['GET'])
def backtest():
    market = request.args.get('market', 'SP500')
    data = fetch_historical_prices(market)
    results = run_backtest(data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
