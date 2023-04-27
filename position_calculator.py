# Acá vamos a intentar crear una calculadora de posicion para tener claramente las posiciones de compra y venta 



class Calculator():

    def __init__(self) -> None:

        self.__capital = 0
        self.__position_size = 0
        self.__equity = 0
        self.__coin_size = 0
        self.__entry = 0
        self.__leverage = 0
        

    def sl_distance(self,capital, risk, leverage, sl, entry_price):


        # Define starting variables
        self.__capital = capital	
        risk = risk
        self.__leverage = leverage
        self.__entry = entry_price

        #Calculate pos based on risk and SL
        self.__position_size = (capital*risk/100)/(sl/100)
        print(f"Pos size USDT: {self.__position_size}")

        # Calculate position size in coin size:
        self.__coin_size = self.__position_size/self.__entry
        print(f"Coin size: {self.__coin_size}")

        # Calculate equity
        self.__equity = self.__position_size/self.__leverage
        print (f"Equity USDT: {self.__equity}")

        # Returns a tuple with the sizes (USDT, coin and equity)
        return self.__position_size, self.__coin_size, self.__equity
    


    def long_entry_exit(self, capital, risk, leverage, entry, exit, sl):
        """
        This method is more precise if you are using TradingView SL tool
        """
        capital = capital	
        risk = risk
        leverage = leverage
        entry = entry
        exit = exit
        self.__position_size = (capital*risk/100)/(sl/100)
        print(self.__position_size)
        return self.__position_size


# aa = Calculator()
# aa.sl_distance(200, 1, 20, 1.01, entry_price=0.6578 )



