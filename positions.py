# Import HTTP from the unified_trading module.
from pybit.unified_trading import HTTP
from pybit.exceptions import InvalidRequestError

from keys import api_key, secret_key
api_key_imported = api_key
secret_key_imported = secret_key

class Position():

    def __init__(self):    

        # Authenticated
        self.__session = HTTP(
        testnet=False,
        api_key=api_key_imported,
        api_secret=secret_key_imported,
        )

        self.__account_balance = "0"


    def get_total_positions(self):
        response = self.__session.get_open_orders(
        category="linear",
        symbol="BNBUSDT",
        )

        print(response)


aa = Position()
aa.get_total_positions()



