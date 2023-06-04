from core.position_calculator import Calculator
from core.send_orders import Order
from controller import Controller
from core.open_orders import Orders
from core.open_positions import Positions
import pandas as pd

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
        self.fees = 0
        self.fees_winning_trade = 0
        self.breakeven_price = None
        

    def get_balance(self):
        self.__account_balance = self.__place_order.get_account_balance()
        return float(self.__account_balance)
    

    def open_long(self, capital, risk, coin, leverage, sl, entry):
        
        # Auto TP defined 2% above entry
        takeprofit = round((102*entry/100), 2)
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

        # Fees calculation assuming SL gets hit
        fees = self.__calculator.fees_calculator()
        self.fees = round(fees[0] + fees[1] , 2)
        self.breakeven_price = round((entry - self.fees), 2)
        self.fees_winning_trade = fees[0] + fees[0]

        


    def open_short(self, capital, risk, coin, leverage, sl, entry):

        # Auto TP defined 2% below entry
        takeprofit = round((98*entry/100), 2)
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

        # Fees calculation assuming SL gets hit
        fees = self.__calculator.fees_calculator()
        self.fees = round(fees[0] + fees[1] ,2 )
        self.breakeven_price = round((entry - self.fees), 2)
        self.fees_winning_trade = fees[0] + fees[0]

        
    def update_orders(self):

        # Get orders and transform to pandas df
        orders_instance = Orders()

        # Check if there are orders and convert to dataframe
        if orders_instance is not None:

            orders = orders_instance.get_open_orders()
            df = pd.DataFrame.from_dict(orders)
            df = df[["symbol", "price", "side", "takeProfit", "stopLoss"]]
            print(df)
            return df

    
    def update_positions(self):

        # Get open positions and transform to df
        positions_instance = Positions()

        # Check if there are positions and convert to dataframe
        if positions_instance is not None:

            positions = positions_instance.get_open_positions()
            df = pd.DataFrame.from_dict(positions)
            df = df[["symbol", "avgPrice", "side", "stopLoss"]]
            return df