import os

from dotenv import load_dotenv
from binance.spot import Spot as Client
from urllib.parse import urlencode
import sys

# Load environment variables from the .env file (if present)
load_dotenv()


class Spot:
    BASEURL = os.getenv("BASEURL_DEV")

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def account_info(self):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.account()
            print(result)
            return result
        except Exception as e:
            print(str(e))
            return None

    def account_info_single(self, asset):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.account()
            result['balances'] = {item['asset']: item for item in result['balances']}
            d_asset = result['balances'][asset]['asset']
            d_free = result['balances'][asset]['free']
            d_locked = result['balances'][asset]['locked']
            return {"asset": d_asset, "free": d_free, "locked": d_locked, "update_time": result['updateTime']}
        except Exception as e:
            print(str(e))
            return None

    def symbol_list(self, asset):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        usdt = []
        count = 20
        try:
            result = client.exchange_info(permissions=["SPOT"])
            data = result['symbols'];
            for i in range(len(data)):
                if data[i]['symbol'].endswith(asset):
                    usdt.append(data[i]['symbol'])
                    if len(usdt) == count:
                        break

            length = len(usdt)
            # if i == length:
            #     break
            # for s in result['symbols']:
            #     if s['symbol'].endswith('USDT'):
            #         usdt.append(s['symbol'])
            print(usdt)
            print(length)
            return usdt
        except Exception as e:
            print(str(e))
            return None

    def order_all(self, symbol, limit):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.get_orders(symbol=symbol, limit=limit)
            return result
        except Exception as e:
            print(str(e))
            return None

    def order_all_in(self):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.get_open_orders()
            return result
        except Exception as e:
            print(str(e))
            return None

    def order(self, symbol, orderId=None, ):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.get_order(symbol, orderId=orderId)
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            result = None
            return result

    def my_trades(self, symbol, orderId=None, startTime=None, endTime=None, fromId=None, limit=None):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.my_trades(symbol, orderId=orderId, startTime=startTime, endTime=endTime, fromId=fromId,
                                      limit=limit)
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            result = None
            return result

    def make_orders(self, symbol, side, type, quantity, price, stop_price):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            params = {"quantity": quantity, "price": price, "stopPrice": stop_price}
            query = urlencode(params)
            result = client.new_order(symbol, side=side, type=type, quantity=quantity, price=price, timeInForce="GTC")
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            result = None
            return result

    def ticker_price_single(self, symbol):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_price(symbol)
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None

    def ticker_price_list(self, symbols):
        params = None
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_price(symbols=symbols)
            print(symbols)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None

    def ticker_price_single24(self, symbol):
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_24hr(symbol)
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None

    def ticker_price_list24(self, symbols):
        params = None
        client = Client(api_key=self.key, api_secret=self.secret)
        if os.getenv("ENV") == "dev":
            client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_24hr(symbols=symbols)
            print(symbols)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None
