import os

from dotenv import load_dotenv
from binance.spot import Spot as Client
from urllib.parse import urlencode
import sys

# Load environment variables from the .env file (if present)
load_dotenv()


class Spot:
    BASEURL = os.getenv("BASEURL")

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def account_info(self):
        client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.account()
            print(result)
            return result
        except Exception as e:
            print(str(e))
            return None

    def order_all(self, symbol, limit):
        client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        # Get server timestamp
        try:
            result = client.get_orders(symbol=symbol, limit=limit)
            return result
        except Exception as e:
            print(str(e))
            return None

    def order(self, symbol, orderId=None, ):
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

    def make_orders(self, symbol,side,type,quantity,price,stop_price):
        client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            params = {"quantity": quantity,"price": price,"stopPrice": stop_price}
            query = urlencode(params)
            result = client.new_order(symbol, side=side, type=type, quantity=quantity,price= price,timeInForce= "GTC")
            print(result)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            result = None
            return result

    def ticker_price_single(self, symbol):
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
        client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_price()
            print(symbols)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None

    def ticker_price_single24(self, symbol):
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
        client = Client(api_key=self.key, api_secret=self.secret, base_url=self.BASEURL)
        try:
            result = client.ticker_24hr()
            print(symbols)
            return result
        except Exception as e:
            print(str(e))  # An exception occurred: ZeroDivisionError
            return None
