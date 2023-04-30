import time

class Controller():

    def __init__(self, view, model):
        self.__view = view
        self.__model = model
        self.coin = None
        self.sl = None
        self.leverage = None
        self.account_balance = None
        self.entry = None
        self.risk = None
        self.connect_signals()


    def connect_signals(self):

        # Press Get Balance button
        self.__view.get_balance_button.clicked.connect(self.get_set_balance)
        
        # Press LONG button
        self.__view.place_long_button.clicked.connect(self.handle_input)
        self.__view.place_long_button.clicked.connect(self.send_long_entry)

        # Press SHORT button
        self.__view.place_short_button.clicked.connect(self.handle_input)
        self.__view.place_short_button.clicked.connect(self.send_short_entry)
    

    def get_set_balance(self):

        # Get account balance
        self.account_balance = self.__model.get_balance()

        # Set accoount balance on GUI
        self.__view.account_balance.setText(str(self.account_balance))


    def handle_input(self):

        # Get symbol from gui
        self.coin = self.__view.coin.text()

        # Get Leverage from gui
        self.leverage = self.__view.leverage.text()
        self.leverage = float(self.leverage)

        # Get SL % from gui
        self.sl = self.__view.stop_loss.text()
        self.sl = float(self.sl)

        # Get Risk from GUI
        self.risk = self.__view.risk_unit.text()
        self.risk = float(self.risk)

        # Get entry price
        self.entry = self.__view.entry.text()
        self.entry = float(self.entry)


    def send_long_entry(self):

        # Execute calculate position and place LONG order
        self.__model.open_long(capital=self.account_balance, risk=self.risk, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )

        # Update GUI
        self.set_placed_order_details()


    def send_short_entry(self):

        # Execute calculate position and place SHORT order
        self.__model.open_short(capital=self.account_balance, risk=self.risk, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )

        # Update GUI
        self.set_placed_order_details()


    def set_placed_order_details(self):

        # Set position size USDT on GUI
        self.__view.position_size.setText(str(self.__model.position_size))
        
        # Set equity USDT on GUI
        self.__view.equity.setText(str(self.__model.equity))

        # Set Auto TP on GUI
        self.__view.auto_tp.setText(str(self.__model.auto_tp))

        # Set Stop loss placed on GUI
        self.__view.stop_loss_palced.setText(str(self.__model.stop_loss))

        # Set order status on GUI
        self.__view.status_label.setText(str(self.__model.order_status))

        # Set breakeven price on GUI
        self.__view.breakeven.setText(str(self.__model.breakeven_price))

        # Set Winning Trade Fees on GUI
        self.__view.w_trade_fee.setText(str(self.__model.fees_winning_trade))

        # Set Losing Trade Fees on GUI
        self.__view.L_trade_fee.setText(str(self.__model.fees))



