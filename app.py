from flask import Flask, render_template, request, jsonify
from stock_scraper import get_stock_price

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_price', methods=['POST'])
def stock_price():
    data = request.json
    symbol = data['symbol']
    price = get_stock_price(symbol)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
