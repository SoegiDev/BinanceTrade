import math

from Libs.Api import Api
from datetime import datetime, timedelta

import time


class Binance:

    def __init__(self, api_key, secret_key):
        self.client = Api(api_key, secret_key)

    def ping_live(self):
        data = self.client.ping()
        return data

    def account_info(self):
        data = []
        balances = self.client.get_account()
        print(balances)
        # for balance in balances['balances']:
        #     if float(balance['locked']) > 0 or float(balance['free']) > 0:
        #         data.append({"asset": balance['asset'], "free": balance['free']})
        #return balances

    def balance(self, asset):
        balances = self.client.get_account()
        balances['balances'] = {item['asset']: item for item in balances['balances']}
        return balances['balances'][asset]['free']

    def history_market(self, market, limit=50):
        data = []
        history = self.client.get_history(market, limit)
        return history

    def server_status(self):
        system_t = int(time.time() * 1000)  # timestamp when requested was launch
        server_t = self.client.get_server_time()  # timestamp when server replied
        lag = int(server_t['serverTime'] - system_t)

        print('System timestamp: %d' % system_t)
        print('Server timestamp: %d' % server_t['serverTime'])
        print('Lag: %d' % lag)
        msg_good = "Good"
        msg_not_good = "Not Good"
        if lag > 1000:
            print('\nNot good. Excessive lag (lag > 1000ms)')
            return msg_not_good
        elif lag < 0:
            print('\nNot good. System time ahead server time (lag < 0ms)')
            return msg_not_good
        else:
            print('\nGood (0ms > lag > 1000ms)')
            return msg_good

    def open_orders(self, market):
        return self.client.get_open_orders(market)

    def tickers(self):
        return self.client.get_all_ticker()

    def market_value(self, symbol, interval, date_s, date_f=""):
        date_s = datetime.strptime(date_s, "%d/%m/%Y %H:%M:%S")

        if date_f != "":
            date_f = datetime.strptime(date_f, "%d/%m/%Y %H:%M:%S")
        else:
            date_f = date_s + timedelta(seconds=59)

        print('Retrieving values...\n')
        klines = self.client.get_klines(symbol, interval, int(date_s.timestamp() * 1000),
                                        int(date_f.timestamp() * 1000))

        if len(klines) > 0:
            for kline in klines:
                timestamp = kline[0]
                open = kline[1]
                high = kline[2]
                low = kline[3]
                close = kline[4]
                return {"timestamp": timestamp, "open": open, "high": high, "low": low, "close": close}
                # return ('[%s] Open: %s High: %s Low: %s Close: %s' % (
                # datetime.fromtimestamp(kline[0] / 1000), kline[1], kline[2], kline[3], kline[4]))

        return

    def step_size_to_precision(ss):
        return ss.find('1') - 1

    def format_value(val, step_size_str):
        precision = Binance.step_size_to_precision(step_size_str)
        return "{:0.0{}f}".format(val, precision)