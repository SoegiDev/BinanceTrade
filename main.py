import urllib.parse

from flask import Flask, render_template, request, jsonify
from Libs.Database import Database
from Binance import Binance
from Libs.Spot import Spot
from urllib.parse import  urlencode
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! BOT TRADE ALREADY STEP ACCOUNT BALANCES</h1>"

#saldklsakdlsakd
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


@app.route('/account-info', methods=['GET'])
def account_info():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    data = Spot(key, secret)
    result = data.account_info()
    # print(data)
    return jsonify({
        "message": result
    })


@app.route('/get-orders', methods=['GET'])
def get_orders():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    limit = request.args.get('limit')
    data = Spot(key, secret)
    result = data.order_all(symbol, limit)
    # print(data)
    return jsonify({
        "message": result
    })


@app.route('/get-order', methods=['GET'])
def get_order():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    orderId = request.args.get('orderId')
    data = Spot(key, secret)
    result = data.order(symbol,orderId)
    # print(data)
    return jsonify({
        "data": result
    })


@app.route('/my-trades', methods=['GET'])
def my_trades():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    orderId = request.args.get('orderId')
    startTime = request.args.get('startTime')
    endTime = request.args.get('endTime')
    fromId = request.args.get('fromId')
    limit = request.args.get('limit')
    data = Spot(key, secret)
    result = data.my_trades(symbol,orderId,startTime,endTime,fromId,limit)
    # print(data)
    return jsonify({
        "data": result
    })

@app.route('/make-orders', methods=['GET'])
def make_orders():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    side = request.args.get('side')
    type = request.args.get('type')
    quantity = request.args.get('quantity')
    price = request.args.get('price')
    stop_price = request.args.get('stop_price')
    data = Spot(key, secret)
    result = data.make_orders(symbol,side,type,quantity,price,stop_price)
    # print(data)
    return jsonify({
        "data": result
    })

@app.route('/get-price-single', methods=['GET'])
def ticker_price_single():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    data = Spot(key, secret)
    result = data.ticker_price_single(symbol)
    # print(data)
    return jsonify({
        "data": result
    })

@app.route('/get-price-list', methods=['GET'])
def ticker_price_list():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbols = request.args.get('symbols')
    data = Spot(key, secret)
    result = data.ticker_price_list(symbols)
    # print(data)
    return jsonify({
        "data": result
    })

@app.route('/get-price-single24', methods=['GET'])
def ticker_price_single24():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    data = Spot(key, secret)
    result = data.ticker_price_single24(symbol)
    # print(data)
    return jsonify({
        "data": result
    })

@app.route('/get-price-list24', methods=['GET'])
def ticker_price_list24():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbols = request.args.get('symbols')
    data = Spot(key, secret)
    result = data.ticker_price_list24(symbols)
    # print(data)
    return jsonify({
        "data": result
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
