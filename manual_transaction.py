""" module that users inputs into a transaction """
from gecko_api import GeckoApi

import datetime
import pytz

class ManualTransaction:
    
    crypto_name = ""
    current_price = 0
    num_coins_trading = 0
    local_date_time = ""
    timezone = ""
    fee = 0
    trade_value = 0
    buy_or_sell = True # default value: True = Buy; False = Sell

    def __init__(self, crypto_name, num_coins_trading, fee, buy_or_sell):
        """
        parameterized constructor which initializes the cryptocurrency name, the number of coins being traded,
        the fee, and whether the transaction is a buy or sell
        """
        self.crypto_name = crypto_name
        self.num_coins_trading = num_coins_trading
        self.fee = 0 # I don't know what this fee is, so for now it will be set to 0
        self.buy_or_sell = buy_or_sell

        """ automatically captures other necessary data """
        self.current_price = GeckoApi(crypto_name).get_attribute("current_price")
        self.trade_value = self.trade_value_format(self.current_price, num_coins_trading)
        self.utc_date_time = datetime.datetime.utcnow() # date time that will be stored
        self.timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        self.local_date_time = datetime.datetime.now()

    def weighted_calculator(self, weight_list, value_list):
        """
        this calculates the average buy or sell of a user's transactions    
        param weight_list: float array | int array
        param value_list: float array | int array
        param buy_sell: Boolean
        """
        sum = 0
        div = 0

        # calculations for weighted average
        for i in range(len(weight_list)):
            sum += (weight_list[i] * value_list[i])
            div += weight_list[i]
        
        return float("{0:.2f}".format(float(sum)/div))


    def return_transaction(self, crypto_name, num_coins_trading, timezone, trade_value, fee, buy_or_sell):
        """ Stores the transaction into a dictionary with a key where it's values is set to [date + time purchased: coin name, the amount] """
        key = str(str(self.utc_date_time) + ": " + crypto_name, num_coins_trading)
        transaction_dictonary = {}
        if key not in transaction_dictonary:
            transaction_dictonary[key] = {self.utc_date_time, timezone, crypto_name, num_coins_trading, trade_value, fee, buy_or_sell}
        return transaction_dictonary


    def quantity_display(self, num_coins_trading, buy_or_sell):
        """ 
        This determines the net change and formats of coins for the transaction
        :param num_coins_trading: int
        :param buy_or_sell: Boolean; True = Buy; False = Sell
        :rtype str
        """
        if buy_or_sell:
            return "\033[92m +{0:.1f}".format(num_coins_trading)
        else:
            return "\033[91m -{0:.1f}".format(num_coins_trading)


    def to_local(self, utc_dt):
        """ 
        converts UTC timezone to user local timezone 
        :param utc_dt: datetime object
        :rtype = datetime obj
        """
        self.local_datetime = utc_dt.replace(tzinfo=pytz.utc)

        local_datetime = self.local_datetime.astimezone(tz=None)

        return local_datetime


    def trade_value_format(self, current_price, num_coins_trading):
        """
        returns the price value in USD of transaction
        calculates price by multiplying current_price and num_coins_trading
        :param current_price: int
        :param num_coins_trading: int
        :rtype float
        """
        return "${0:.2f}".format(current_price * num_coins_trading)


# for testing
# if __name__ == "__main__":
#     LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
#     dt = datetime.datetime.now() # is the current time zone
    
#     # print("key: " + str(date_time) + " " + "crypto_name", "num_coins_trading")
#     utc_dt = datetime.datetime.utcnow()
    
#     mt = ManualTransaction("Bitcoin", 2, 0, True)

#     print("current UTC date and time: " + str(utc_dt))
#     print("UTC to local conversion: " + str(mt.to_local(utc_dt)))
    
#     # print(str(dt))
#     print(LOCAL_TIMEZONE)

    
        
