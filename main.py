from flask import Flask, render_template, request, jsonify
from Libs.Database import Database
from Binance import Binance

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! BOT TRADE ALREADY STEP ACCOUNT BALANCES</h1>"


@app.route('/initdb')
def initDB():
    try:
        Database.create_table()
        result = "Initialitation Database is SUccessfully"
        return jsonify({
            "data": result
        })
    except Exception as e:
        # print('bl: %s' % (e))
        result = e
        return jsonify({
            "data": result
        })


@app.route('/ping', methods=['GET'])
def ping():
    key = request.args.get('key')
    secret = request.args.get('secret')
    bin = Binance(key, secret)
    data = bin.ping_live()
    result = 200
    if data == 200:
        result = 200
    else:
        result = 400
    # print(data)
    return jsonify({
        "data": result
    })


@app.route('/balances', methods=['GET'])
def account_balances():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    bin = Binance(key, secret)
    data = bin.balances()
    # print(data)
    return jsonify({
        "data": data
    })


@app.route('/balance', methods=['GET'])
#ASSET=BTC
def account_balance():
    key = request.args.get('key')
    secret = request.args.get('secret')
    asset = request.args.get('asset')
    bin = Binance(key, secret)
    data = bin.balance(asset)
    # print(data)
    return jsonify({
        "data": data
    })


@app.route('/history', methods=['GET'])
#MARKET=BTCUSDT$LIMIT=1000
def history_market():
    key = request.args.get('key')
    secret = request.args.get('secret')
    market = request.args.get('market')
    limit = request.args.get('limit')
    bin = Binance(key, secret)
    data = bin.history_market(market, limit)
    # print(data)
    return jsonify({
        "data": data
    })


@app.route('/open_orders', methods=['GET'])
#MARKET=BTCUSDT
def open_orders():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    market = request.args.get('market')
    bin = Binance(key, secret)
    data = bin.open_orders(market)
    # print(data)
    return jsonify({
        "data": data
    })


@app.route('/tickers', methods=['GET'])
def tickers():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    data = Binance(key, secret)
    result = data.tickers()
    # print(data)
    return jsonify({
        "data": result
    })


@app.route('/market_value_range',methods=['GET'])
def check_market_range():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    interval = request.args.get('interval')
    start_time = request.args.get('start-time')
    end_time = request.args.get('end-time')

    data = Binance(key, secret)
    result = data.market_value(symbol,interval,start_time,end_time)
    # print(data)
    return jsonify({
        "data": result
    })


@app.route('/server_check', methods=['GET'])
def check_server():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    data = Binance(key, secret)
    result = data.server_status()
    # print(data)
    return jsonify({
        "message": result
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
