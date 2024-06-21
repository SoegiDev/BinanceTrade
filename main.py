import urllib.parse

from flask import Flask, render_template, request, jsonify
from Libs.Database import Database
from Binance import Binance
from Libs.Spot import Spot
from urllib.parse import urlencode

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
        "data": result
    })


@app.route('/account-info-single', methods=['GET'])
def account_info_single():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    asset = request.args.get('asset')
    data = Spot(key, secret)
    result = data.account_info_single(asset)
    return jsonify({
        "data": result
    })


@app.route('/symbol-list', methods=['GET'])
def symbol_list():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    asset = request.args.get('asset')
    data = Spot(key, secret)
    result = data.symbol_list(asset)
    # print(data)
    return jsonify({
        "data": result
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
        "data": result
    })


@app.route('/get-order', methods=['GET'])
def get_order():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    orderId = request.args.get('orderId')
    data = Spot(key, secret)
    result = data.order(symbol, orderId)
    # print(data)
    return jsonify({
        "data": result
    })


@app.route('/get-order-all', methods=['GET'])
def get_order_all():
    # SPOT #
    key = request.args.get('key')
    secret = request.args.get('secret')
    data = Spot(key, secret)
    result = data.order_all_in()
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
    result = data.my_trades(symbol, orderId, startTime, endTime, fromId, limit)
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
    result = data.make_orders(symbol, side, type, quantity, price, stop_price)
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
    symbol = request.args.get('symbol')
    data = Spot(key, secret)
    data_symbol = data.symbol_list(symbol)
    result = data.ticker_price_list(data_symbol)
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
    list_s = []
    key = request.args.get('key')
    secret = request.args.get('secret')
    symbol = request.args.get('symbol')
    data = Spot(key, secret)
    data_symbol = data.symbol_list(symbol)
    result = data.ticker_price_list24(data_symbol)
    for pet in result:
        list_s.append(pet)
    for i in range(len(list_s)):
        list_s[i]['agg'] = data.agg_trades(list_s[i]['symbol'])[0]
    # for i, pet11 in enumerate(list_s):
    #     list_s[i]['detail'] = pet11[i]['symbol']
    #     list_s.append(list_s[i]['detail'])
    # for i, x in enumerate(list_s):
    #     list_s[i]['detail'] = x[i]['symbol']
    #     list_s.append(list_s[i]['detail'] )
    # DD= data.agg_trades('DOGEUSDT')
    # print(data)
    return jsonify({
        "data": list_s
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
