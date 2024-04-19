from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    # Parse request data
    request_data = request.get_json()
    ticker = request_data.get('ticker')
    period = request_data.get('period')

    if not ticker or not period:
        return jsonify({"error": "Please provide both 'ticker' and 'period'"}), 400

    # Fetch data
    data = yf.Ticker(ticker)
    hist = data.history(period=period)

    if hist.empty:
        return jsonify({"error": "No data found"}), 404

    # Specify the order of columns
    columns_order = ['Date', 'Low', 'Open', 'Close', 'High']
    # Reorder DataFrame and convert to 2D list
    ordered_data = hist.reset_index()[columns_order].values.tolist()

    return jsonify({"data": ordered_data})


if __name__ == '__main__':
    app.run(debug=True)
