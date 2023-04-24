
# Import HTTP from the unified_trading module.
from pybit.unified_trading import HTTP

"""
You can create an authenticated or unauthenticated HTTP session. 
You can skip authentication by not passing any value for the key and secret.
"""

# Import your keys from a .py or .txt file. Use the name api_key and secret_key
from keys import api_key, secret_key
api_key_imported = api_key
secret_key_imported = secret_key


class Order():

    def __init__(self):
        
        # Authenticated
        self.__session = HTTP(
        testnet=False,
        api_key=api_key_imported,
        api_secret=secret_key_imported,
        )

        self.__account_balance = "0"
        self.get_account_balance()


    def get_account_balance(self):
        # Get wallet balance of the Unified Trading Account
        self.__account_balance = self.__session.get_wallet_balance(accountType="CONTRACT")
        self.__account_balance = self.__account_balance["result"]["list"][0]["coin"][0]["equity"]
        print(f"El balance de su cuenta es: {self.__account_balance}.")
        return self.__account_balance
        
        
# Acá me doy cuenta que la moneda tiene que tener habilitado el hedge mode para que el positionIdx funcione.
# Si no tienes habilitado el hedge mode para cierto PAR, no va a funcionar el positionIdx=1, tienes que usar el 0 que es one way position 
# Tenemos que validar previamente que tipo de trading tienes para la moneda particular, y poder calcular
# positionIdx :
#   0 one-way mode position
#   1 Buy side of hedge-mode position
#   2 Sell side of hedge-mode position      

    def open_long(self, price, tp, sl,  coin="BTCUSDT", order_type="Limit", size=0.001):
        # Place an order on that USDT Perpetual
        print(self.__session.place_order(
            category="linear",
            symbol=coin,
            side="Buy",
            orderType=order_type,
            qty = size,
            price=price,
            takeProfit=tp,
            stopLoss=sl,
            positionIdx=1
        ))


    def open_short(self, price, tp, sl,  coin="BTCUSDT", order_type="Limit", size=0.001):
        # Place an order on that USDT Perpetual
        print(self.__session.place_order(
            category="linear",
            symbol=coin,
            side="Sell",
            orderType=order_type,
            qty = size,
            price=price,
            takeProfit=tp,
            stopLoss=sl,
            positionIdx=2,
        ))

prueba = Order()
prueba.open_long("0.6578", tp="0.72625", sl="0.65115", coin="IDUSDT", size=301)

"""
prueba = Order()
prueba.open_long("26430.7", tp="29563", sl="25778", size=0.002)

prueba.open_short("30149.86", tp="28981.33", sl="30980.38", size=0.003)
prueba.get_account_balance()

"""

