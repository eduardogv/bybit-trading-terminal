from position_calculator import Calculator
from send_orders import Order
from controller import Controller

class Model():

    def __init__(self) -> None:
        self.__place_order = Order()
        self.__calculator = Calculator()
        self.__leverage = None
        self.__position_size = 0
        self.__coin_size = 0
        self.__equity = 0
        self.__entry = 0
        self.__account_balance = 0
        

    def get_balance(self):
        self.__account_balance = self.__place_order.get_account_balance()
        print(self.__account_balance)
        return float(self.__account_balance)
        
        

    def open_long(self, capital, coin, leverage, sl, entry):
        
        # Auto TP defined 7% above entry
        takeprofit = round((107*entry/100), 2)

        # Stop Loss calculated from input
        stoploss = round(entry*((100-sl)/100), 2)

        #Calculate Size using position_calculator module
        position_sizes = self.__calculator.sl_distance(capital=capital, risk=1, leverage=leverage, sl=sl, entry_price=entry)
        
        # Place order
        self.__place_order.open_long(price=entry, tp=takeprofit, sl=stoploss, coin=coin, order_type="Limit", size=round(position_sizes[1], 4) )
        
        
    def open_short(self, coin, leverage, sl, entry):

        #print("place_order clicked")
        pass
        
        
