from Libs.Api import Api
from datetime import datetime,timedelta

import time
class Binance:

    def __init__(self, api_key, secret_key):
        self.client = Api(api_key, secret_key)

    def ping_live(self):
        data = self.client.ping()
        return data
    def balances(self):
        data = []
        balances = self.client.get_account()
        for balance in balances['balances']:
            if float(balance['locked']) > 0 or float(balance['free']) > 0:
                print('%s: %s' % (balance['asset'], balance['free']))
                data.append({"asset":balance['asset'], "free":balance['free']})
        return data


    def balance(self, asset):

        balances = self.client.get_account()
        balances['balances'] = {item['asset']: item for item in balances['balances']}
        print(balances['balances'][asset]['free'])
        return balances['balances'][asset]['free']

    def history_market(self,market,limit=50):
        data = []
        history = self.client.get_history(market,limit)
        return history

    def server_status(self):
        systemT = int(time.time() * 1000)  # timestamp when requested was launch
        serverT = self.client.get_server_time()  # timestamp when server replied
        lag = int(serverT['serverTime'] - systemT)

        print('System timestamp: %d' % systemT)
        print('Server timestamp: %d' % serverT['serverTime'])
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
        return

    def open_orders(self,market):
        return self.client.get_open_orders(market)

    def tickers(self):
        return self.client.get_all_ticker()

    def market_value(self, symbol, interval, date_s , date_f=""):
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
                return {"timestamp":timestamp,"open":open,"high":high,"low":low,"close":close}
                # return ('[%s] Open: %s High: %s Low: %s Close: %s' % (
                # datetime.fromtimestamp(kline[0] / 1000), kline[1], kline[2], kline[3], kline[4]))

        return