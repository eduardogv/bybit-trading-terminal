from position_calculator import Calculator
from send_orders import Order
from controller import Controller

class Model():

    def __init__(self) -> None:
        self.__place_order = Order()
        self.__calcultor = Calculator()
        self.__position_size = 0
        self.__coin_size = 0
        self.__equity = 0
        self.__entry = 0
        self.__account_balance = 0
        

    def place_order(self, entry):
        entry = self.__entry
        self.__account_balance = 0
        self.calculate_pos()

    
    def calculate_pos(self):

        # Calculate position values from tuple 
        self.__position_size, self.__coin_size, self.__equity = self.__calcultor.sl_distance(200, 1, 20, 1.01, entry_price=self.__entry)

    def place_order(self):
        pass
        




    
    # def place_order(self):
    #     self.__position_size = self.__calcultor.sl_distance(capital= 200 , risk= 1, leverage= 20, sl= 1.01)
    #     print(self.__position_size)
    #     return self.__position_size


bb = Model()
#bb.place_order()

