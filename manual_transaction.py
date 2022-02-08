""" module that users inputs into a transaction """
from gecko_api import GeckoApi

import tkinter
from tkinter import *
import datetime
from time import time

""" temporary for compile until user interface is made """
root = tkinter.Tk()

crypto_name_str = tkinter.StringVar()
num_coins_trading_int = tkinter.IntVar()
buy_or_sell_Bool = tkinter.BooleanVar()


def store_transaction():
    global crypto_name
    global current_price 
    global num_coins_trading
    global date_time
    global timezone
    global fee
    global trade_value
    # True = Buy; False = Sell
    global buy_or_sell

    """ logic that capturs user input"""
    crypto_name = crypto_name_str.get()
    num_coins_trading = num_coins_trading_int.get()
    buy_or_sell = buy_or_sell_Bool.get()
    
    date_time = str(datetime.datetime.now())
    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    trade_value = trade_value_format()
    """ I have no idea how the fee is calculated"""
    fee = 0

    # retrieves current price of cryptocurrency
    current_price = GeckoApi(crypto_name).get_attribute("current_price")

    """ Clears entries """
    crypto_name_str.set("")
    num_coins_trading_int.set(0)
    buy_or_sell_Bool.set(True) # default value is Buy
    
    return_transaction()


def return_transaction():
    """ Stores the transaction into a dictionary with a key where it's values is set to [date + time purchased: coin name, the amount] """
    key = str(str(date_time) + ": " + crypto_name, num_coins_trading)
    transaction_dictonary = {}
    if key not in transaction_dictonary:
        transaction_dictonary[key] = {date_time, timezone, crypto_name, num_coins_trading, trade_value, fee, buy_or_sell}
    return transaction_dictonary

def quantity_display():
    """ 
    This determines the net change and formats of coins for the transaction
    rtype: str
    """

    # Declares ansi escape characters
    green = '\033[92m'
    red = "\033[91m"

    if buy_or_sell:
        return green + "+{0:.1f}".format(num_coins_trading) 
    else:
        return red + "-{0:.1f}".format(num_coins_trading)

def trade_value_format():
    """
    returns the price value in USD of transaction
    calculates price by multiplying current_price and num_coins_trading
    rtype: int
    """
    return "${0:.2f}".format(current_price * num_coins_trading)

# for testing
if __name__ == "__main__":
    LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    dt = datetime.datetime.now()
    
    # date_time = datetime.datetime.now()
    # print("key: " + str(date_time) + " " + "crypto_name", "num_coins_trading")
    print(str(dt))
    print(LOCAL_TIMEZONE)

    
        
