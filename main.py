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


@app.route('/balances',methods=['GET'])
def account_balances():
    # SPOT #
    api_key_spot_tes = "LTSd8ozvwoH152vg9LvM0BC4dD09DO4Tlkjdf8eyCIwhWa8aDVtlxboJ1oUdDPi9"
    secret_key_spot_tes = "H4wBD9yw1uJIICBycEX6ddLh3UVWG5dTamy6OkcxpAjQb1mCAowjYisOgmE7DE8o"
    key = request.args.get('key')
    secret = request.args.get('secret')
    bin = Binance(key,secret)
    data = bin.balances()
    # print(data)
    return jsonify({
        "data": data
    })

@app.route('/balance', methods=['GET'])
#ASSET=BTC
def account_balance():
    # SPOT #
    api_key_spot_tes = "LTSd8ozvwoH152vg9LvM0BC4dD09DO4Tlkjdf8eyCIwhWa8aDVtlxboJ1oUdDPi9"
    secret_key_spot_tes = "H4wBD9yw1uJIICBycEX6ddLh3UVWG5dTamy6OkcxpAjQb1mCAowjYisOgmE7DE8o"
    key = request.args.get('key')
    secret = request.args.get('secret')
    asset = request.args.get('asset')
    bin = Binance(key,secret)
    data = bin.balance(asset)
    # print(data)
    return jsonify({
        "data": data
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
