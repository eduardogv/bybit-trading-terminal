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
        self.tab_index = None
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

        # Press UPDATE button
        self.__view.upate_orders_button.clicked.connect(self.handle_input)
        self.__view.upate_orders_button.clicked.connect(self.update_orders_and_positions)
    

    def get_set_balance(self):

        # Get account balance
        self.account_balance = self.__model.get_balance()

        # Set accoount balance on GUI
        self.__view.account_balance.setText(str(self.account_balance))


    def handle_input(self):

        # Get Accoun Balance from GUI if button not clicked
        self.account_balance = float(self.__view.account_balance.text())

        # Get tab index from GUI
        self.tab_index = self.__view.tabWidget.currentIndex()
        print (type(self.tab_index))

        # Get symbol from GUI
        self.coin = self.__view.coin.text()

        # Get Leverage from GUI
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

        # Execute calculate position and place LONG order Quick Mode
        if self.tab_index == 0:
            self.__model.open_long(capital=self.account_balance, risk=self.risk, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )
        if self.tab_index == 1:
            print("Estas en modo normal")

        # Update GUI
        self.set_placed_order_details()


    def send_short_entry(self):

        # Execute calculate position and place SHORT order
        self.__model.open_short(capital=self.account_balance, risk=self.risk, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )

        # Update GUI
        self.set_placed_order_details()


    def update_orders_and_positions(self):

        # Execute update orders 
        try:
            orders_df = self.__model.update_orders()
            self.__view.set_orders(orders_df)
        except:
            print("no data for orders")

        # Execute  update positions
        try:
            positions_df = self.__model.update_positions()
            self.__view.set_positions(positions_df)
        except:
            print("no data for positions")


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



