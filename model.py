from position_calculator import Calculator
from send_orders import Order
from controller import Controller

class Model():

    def __init__(self) -> None:
        self.__place_order = Order()
        self.__calcultor = Calculator()
        self.__position_size = 0

    
    def place_order(self):
        self.__position_size = self.__calcultor.sl_distance(capital= 200 , risk= 1, leverage= 20, sl= 1.01)
        print(self.__position_size)
        return self.__position_size


bb = Model()
bb.place_order()




    

