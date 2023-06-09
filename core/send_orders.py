
# Import HTTP from the unified_trading module.
from pybit.unified_trading import HTTP
from pybit.exceptions import InvalidRequestError

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


    def get_account_balance(self):
        
        # Get wallet balance of the Normal Trading Account
        self.__account_balance = self.__session.get_wallet_balance(accountType="CONTRACT")
        self.__account_balance = self.__account_balance["result"]["list"][0]["coin"][0]["equity"]
        return self.__account_balance


    def open_long(self, price, tp, sl,  coin="BTCUSDT", order_type="Limit", size=0.001):
        """
        positionIdx :
        0 one-way mode position
        1 Buy side of hedge-mode position
        2 Sell side of hedge-mode position 
        """
        # Place an order on that USDT Perpetual
        if tp>price>sl:
            try:
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
                result = "LONG order placed succesfully. Good luck degen!"
                return result
                
            except InvalidRequestError as e:
                    print(repr(e))
                    #print("Se ha tenido un error por el positionIdx")
        else:
            print("No se cumple TP>Price>SL")


    def open_short(self, price, tp, sl,  coin="BTCUSDT", order_type="Limit", size=0.001):
        """
        positionIdx :
        0 one-way mode position
        1 Buy side of hedge-mode position
        2 Sell side of hedge-mode position 
        """
        
        # Place an order on that USDT Perpetual
        if sl>price>tp:
            try:
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
                result = "SHORT order placed succesfully. Good luck degen!"
                return result
            
            except InvalidRequestError as e:
                print(repr(e))
                print("Se ha tenido un error por el positionIdx")
        else:
            print("No se cumple SL>price>TP")



# Faltaría validar el modo hedge o one-way en cada symbol, vale la pena hacerlo?
# Falta definir el leverage de cada posición
