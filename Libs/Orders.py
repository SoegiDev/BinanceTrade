# -*- coding: UTF-8 -*-
# @yasinkuyu
from Api import Api
from Messages import Messages

from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Define Custom import vars
client = Api(os.getenv("api_key"), os.getenv("secret_key"))


class Orders():

    @staticmethod
    def buy_limit(symbol, quantity, buyPrice):

        order = client.buy_limit(symbol, quantity, buyPrice)

        if 'msg' in order:
            Messages.get(order['msg'])

        # Buy order created.
        return order['orderId']

    @staticmethod
    def sell_limit(symbol, quantity, sell_price):

        order = client.sell_limit(symbol, quantity, sell_price)

        if 'msg' in order:
            Messages.get(order['msg'])

        return order