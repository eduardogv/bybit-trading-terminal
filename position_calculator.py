# Acá vamos a intentar crear una calculadora de posicion para tener claramente las posiciones de compra y venta 



class Calculator():

    def __init__(self) -> None:

        self.__capital = 0
        self.__position_size = 0
        self.__equity = 0
        

    def sl_distance(self,capital, risk, leverage, sl):
        capital = capital	
        risk = risk
        leverage = leverage
        self.__position_size = (capital*risk/100)/(sl/100)
        print(self.__position_size)
        return self.__position_size

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



aa = Calculator()
aa.sl_distance(200, 1, 20, 1.01)


