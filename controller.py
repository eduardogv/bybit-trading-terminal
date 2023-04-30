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
        #print (f"account balance: {self.account_balance}")

        # Set accoount balance on GUI
        self.__view.account_balance.setText(str(self.account_balance))


    def handle_input(self):

        #Get account balance (parece que no lo necesito)
        # self.account_balance = self.__model.get_balance()
        # print (f"account balance: {self.account_balance}")
        
        # Get symbol from gui
        self.coin = self.__view.coin.text()

        # Get Leverage from gui
        self.leverage = self.__view.leverage.text()
        self.leverage = float(self.leverage)

        # Get SL % from gui
        self.sl = self.__view.stop_loss.text()
        self.sl = float(self.sl)

        # Get entry price
        self.entry = self.__view.entry.text()
        self.entry = float(self.entry)


    def send_long_entry(self):

        # Execute calculate position and place LONG order
        self.__model.open_long(capital=self.account_balance, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )
        #print(self.__model.auto_tp)
        #print("long entry")
        time.sleep(4)
        self.set_placed_order_details()



    def send_short_entry(self):

        # Execute calculate position and place SHORT order
        self.__model.open_short(capital=self.account_balance, coin=self.coin, leverage=self.leverage, sl=self.sl, entry=self.entry )
        #print("short entry")


    def set_placed_order_details(self):

        # Set position size USDT on GUI
        self.__view.position_size.setText(str(self.__model.position_size))
        
        # Set equity USDT on GUI
        self.__view.equity.setText(str(self.__model.equity))

        # Set Auto TP on GUI
        self.__view.auto_tp.setText(str(self.__model.auto_tp))

        # Set Stop loss placed on GUI
        self.__view.stop_loss_palced.setText(str(self.__model.stop_loss))