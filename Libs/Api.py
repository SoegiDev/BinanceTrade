import logging
import time
import hashlib
import requests
import hmac
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

try:
    from urllib import urlencode
# python3
except ImportError:
    from urllib.parse import urlencode

class Api:
    BASE_URL = "https://www.binance.com/api/v1"
    BASE_URL_V3 = "https://api.binance.com/api/v3"
    BASE_URL_V3_TES = "https://testnet.binance.vision/api/v3"
    PUBLIC_URL = "https://www.binance.com/exchange/public/product"

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    #PING SERVER
    def ping(self):
        path = "%s/ping" % self.BASE_URL_V3_TES
        return requests.get(path, timeout=30, verify=True).status_code

    #GET HISTORY
    def get_history(self, market, limit=50):
        path = "%s/aggTrades" % self.BASE_URL_V3_TES
        params = {"symbol": market, "limit": limit}
        return self._get_no_sign(path, params)

    def get_order_books(self, market, limit=50):
        path = "%s/depth" % self.BASE_URL_V3_TES
        params = {"symbol": market, "limit": limit}
        return self._get_no_sign(path, params)

    def get_account(self):
        path = "%s/account" % self.BASE_URL_V3_TES
        return self._get(path, {})

    def get_products(self):
        path = "%s/exchangeInfo" % self.BASE_URL_V3_TES
        params = {}
        return self._get_no_sign(path, params)
        # return requests.get(self.BASE_URL_V3_TES, timeout=30, verify=True).json()




    def get_all_ticker(self):
        path = "%s/ticker/24hr" % self.BASE_URL_V3_TES
        params = {}
        return self._get_no_sign(path, params)

    def buy_limit(self, market, quantity, rate):
        path = "%s/order" % self.BASE_URL_V3
        params = self._order(market, quantity, "BUY", rate)
        return self._post(path, params)

    def get_klines(self, market, interval, startTime, endTime):
        path = "%s/klines" % self.BASE_URL_V3_TES
        params = {"symbol": market, "interval": interval, "startTime": startTime, "endTime": endTime}
        return self._get_no_sign(path, params)

    def sell_limit(self, market, quantity, rate):
        path = "%s/order" % self.BASE_URL_V3
        params = self._order(market, quantity, "SELL", rate)
        return self._post(path, params)

    def _order(self, market, quantity, side, rate=None):
        params = {}

        if rate is not None:
            params["type"] = "LIMIT"
            params["price"] = self._format(rate)
            params["timeInForce"] = "GTC"
        else:
            params["type"] = "MARKET"

        params["symbol"] = market
        params["side"] = side
        params["quantity"] = '%.8f' % quantity

        return params

    def _delete(self, path, params=None):
        if params is None:
            params = {}
        params.update({"recvWindow": os.getenv('recv_window')})
        query = urlencode(self._sign(params))
        url = "%s?%s" % (path, query)
        header = {"X-MBX-APIKEY": self.key}
        return requests.delete(url, headers=header,timeout=30, verify=True).json()

    def get_server_time(self):
        path = "%s/time" % self.BASE_URL_V3_TES
        return requests.get(path, timeout=30, verify=True).json()

    def get_exchange_info(self):
        path = "%s/exchangeInfo" % self.BASE_URL_V3_TES
        return requests.get(path, timeout=30, verify=True).json()

    def get_open_orders(self, market):
        path = "%s/openOrders" % self.BASE_URL_V3_TES
        params = {"symbol": market}
        return self._get(path, params)

    def _format(self, price):
        return "{:.8f}".format(price)

    def _get_no_sign(self, path, params={}):
        query = urlencode(params)
        url = "%s?%s" % (path, query)
        return requests.get(url, timeout=30, verify=True).json()

    def _sign(self, params={}):
        data = params.copy()

        ts = int(1000 * time.time())
        data.update({"timestamp": ts})
        h = urlencode(data)
        b = bytearray()
        b.extend(self.secret.encode())
        signature = hmac.new(b, msg=h.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
        data.update({"signature": signature})
        return data

    def _get(self, path, params=None):
        if params is None:
            params = {}
        params.update({"recvWindow": os.getenv("recv_window")})
        query = urlencode(self._sign(params))
        url = "%s?%s" % (path, query)
        header = {"X-MBX-APIKEY": self.key}
        return requests.get(url, headers=header,timeout=30, verify=True).json()

    def _post(self, path, params=None):
        if params is None:
            params = {}
        params.update({"recvWindow": os.getenv("recv_window")})
        query = urlencode(self._sign(params))
        url = "%s" % (path)
        header = {"X-MBX-APIKEY": self.key}
        return requests.post(url, headers=header, data=query,timeout=30, verify=True).json()
