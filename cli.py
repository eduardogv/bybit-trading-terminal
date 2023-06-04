from core.position_calculator import Calculator
from core.send_orders import Order

# Initialize classes
order_class = Order()
calculator_class = Calculator()





def main():
    


    # initialize global variables
    account_balance = float(200)
    choice = 0
    risk = float(1)

    # Main Loop
    while choice !=6:
        
        print("-------------------------------------")
        print("*** Bybit Trading Terminal ***")
        print ("l) Account Balance and Risk %")
        print("2) Open LONG")
        print("3) Open SHORT")
        print("4) Get Open Orders")
        print("5) Get Open Positions")
        print("6) Quit")
        print("7) Stats and debug")
        print("-------------------------------------")
        choice  = int(input())

        # 1)Get Account Balance or set Trading balance
        if choice == 1:
            choice_1 = 0
            while choice_1 != 4: 
                print("-------------------------------------")
                print("*** Get Account Balance or set Trading balance ***")
                print("l) Get Account Balance from Bybit")
                print("2) Set Manual Account Balance")
                print("3) Set Manual Risk %")
                print("4) Go Back to Main Menu") 
                choice_1  = int(input())
                print("-------------------------------------")

                if choice_1 == 1:
                    account_balance = order_class.get_account_balance()
                    print ("Account Balance set to: " + account_balance)
                
                elif choice_1 == 2:
                    account_balance = input("Enter manual account balance: ")
                    account_balance = float(account_balance)
                
                elif choice_1 == 3:
                    risk = input("Enter manual risk, default 1: ")
                    risk = float(risk)
        
        # 2) Open Long
        if choice == 2:
            choice_2 = 0
            while choice_2 != 4: 
                print("-------------------------------------")
                print("*** Open LONG ***")
                print("l) Enter Position Parameters")
                print("2) Check Parameters")
                print("3) Enter Position") 
                print("4) Go Back to Main Menu")
                choice_2  = int(input())
                print("-------------------------------------")
                
                # 1) Enter position parameters
                if choice_2 == 1:
                    coin = input("Enter Coin: ")
                    coin = coin.upper()+ "USDT"
                    entry = float(input("Enter entry price: "))
                    stop_loss_distance = float(input("Enter Stop Loss %: "))
                    take_profit = float(input("Enter Take Profit: "))

                # 2) Check Parameters      
                elif choice_2 == 2:
                    print ("** Your positions parameters**")
                    print (coin)
                
                # 3) Enter Position
                elif choice_2 == 3:
                    try:
                        new_order = open_long(capital=account_balance, risk=risk, coin=coin, leverage=20, stoploss_distance=stop_loss_distance, tp_price=take_profit, entry=entry)
                    except:
                        print("Error, something happenned")

        # 3) Open Short
        if choice == 3:
            choice_2 = 0
            while choice_2 != 4: 
                print("-------------------------------------")
                print("*** Open LONG ***")
                print("l) Enter Position Parameters")
                print("2) Check Parameters")
                print("3) Enter Position") 
                print("4) Go Back to Main Menu")
                choice_2  = int(input())
                print("-------------------------------------")
                
                # 1) Enter position parameters
                if choice_2 == 1:
                    coin = input("Enter Coin: ")
                    coin = coin.upper()+ "USDT"
                    entry = float(input("Enter entry price: "))
                    stop_loss_distance = float(input("Enter Stop Loss %: "))
                    take_profit = float(input("Enter Take Profit: "))

                # 2) Check Parameters      
                elif choice_2 == 2:
                    print ("** Your positions parameters**")
                    print (coin)
                
                # 3) Enter Position
                elif choice_2 == 3:
                    try:
                        new_order = open_long(capital=account_balance, risk=risk, coin=coin, leverage=20, stoploss_distance=stop_loss_distance, tp_price=take_profit, entry=entry)
                    except:
                        print("Error, something happenned")            
        
        # Debug option
        if choice == 7:
            print("Account Balance: " + str(account_balance))
            print("Risk: " + str(risk))





# Depende de position calculator
def open_long(capital, risk, coin, leverage, stoploss_distance, tp_price, entry):
                
        # Take Profit from input  

        # Stop Loss calculated from input
        stoploss_price = round(entry-(entry*stoploss_distance/100), 2)

        #Calculate Size using position_calculator (pos size, coin size, equity size)
        position_sizes = calculator_class.sl_distance(capital=capital, risk=risk, leverage=leverage, sl=stoploss_distance, entry_price=entry)
        print("capital: "+ str(capital))
        print("risk: "+ str(risk))
        print("leverage: "+ str(leverage))
        print("sl: "+ str(stoploss_distance))
        print("entry_price: "+ str(entry))
        print (position_sizes)
        
        # Place order
        order = order_class.open_long(price=entry, tp=tp_price, sl=stoploss_price, coin=coin, order_type="Limit", size=round(position_sizes[1], 4) )

        # # Long details
        # position_size = round(position_sizes[0], 1) 
        # equity = round(position_sizes[2], 1) 

        # # Fees calculation assuming SL gets hit
        # fees = calculator_class.fees_calculator()
        # self.fees = round(fees[0] + fees[1] , 2)
        # self.breakeven_price = round((entry - self.fees), 2)
        # self.fees_winning_trade = fees[0] + fees[0]





if __name__ == "__main__":
    main()
