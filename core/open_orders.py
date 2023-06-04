# Import HTTP from the unified_trading module.
from pybit.unified_trading import HTTP
from pybit.exceptions import InvalidRequestError

from keys import api_key, secret_key
api_key_imported = api_key
secret_key_imported = secret_key

class Orders():

    def __init__(self):    

        # Authenticated
        self.__session = HTTP(
        testnet=False,
        api_key=api_key_imported,
        api_secret=secret_key_imported,
        )

        self.__account_balance = "0"


    def get_open_orders(self):

        response = self.__session.get_open_orders(
            category="linear", 
            #symbol = "BTCUSDT",
            openOnly=0,
            limit=50,
            settleCoin = "USDT"
        )

        orders = response["result"]["list"]
        #print(orders)
        return orders

def get_orders():
    instance = Orders()
    a = instance.get_open_orders()
    return a
