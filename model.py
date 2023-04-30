from position_calculator import Calculator
from send_orders import Order
from controller import Controller

class Model():

    def __init__(self) -> None:
        self.__place_order = Order()
        self.__calculator = Calculator()
        self.__leverage = 0
        self.position_size = 0
        self.__coin_size = 0
        self.equity = 0
        self.__entry = 0
        self.auto_tp = 0
        self.stop_loss = 0
        self.__take_profit = 0
        self.__account_balance = 0
        self.order_status = None
        

    def get_balance(self):
        self.__account_balance = self.__place_order.get_account_balance()
        return float(self.__account_balance)
    

    def open_long(self, capital, risk, coin, leverage, sl, entry):
        
        # Auto TP defined 7% above entry
        takeprofit = round((107*entry/100), 2)
        self.auto_tp = takeprofit        

        # Stop Loss calculated from input
        stoploss = round(entry-(entry*sl/100), 2)
        self.stop_loss = stoploss

        #Calculate Size using position_calculator (pos size, coin size, equity size)
        position_sizes = self.__calculator.sl_distance(capital=capital, risk=risk, leverage=leverage, sl=sl, entry_price=entry)
        
        # Place order
        order = self.__place_order.open_long(price=entry, tp=takeprofit, sl=stoploss, coin=coin, order_type="Limit", size=round(position_sizes[1], 4) )
        self.order_status = order

        # Long details
        self.position_size = round(position_sizes[0], 1) 
        self.equity = round(position_sizes[2], 1) 


    def open_short(self, capital, risk, coin, leverage, sl, entry):

        # Auto TP defined 5% above entry
        takeprofit = round((95*entry/100), 2)
        self.auto_tp = takeprofit  

        # Stop Loss calculated from input
        stoploss = round(entry+(entry*sl/100), 2)
        self.stop_loss = stoploss

        #Calculate Size using position_calculator module
        position_sizes = self.__calculator.sl_distance(capital=capital, risk=risk, leverage=leverage, sl=sl, entry_price=entry)
        
        # Place order
        order = self.__place_order.open_short(price=entry, tp=takeprofit, sl=stoploss, coin=coin, order_type="Limit", size=round(position_sizes[1], 4) )
        self.order_status = order

        # Short details
        self.position_size = round(position_sizes[0], 1) 
        self.equity = round(position_sizes[2], 1) 
        
        
        
