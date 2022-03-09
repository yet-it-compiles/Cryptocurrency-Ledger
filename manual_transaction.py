""" module that users inputs into a transaction """
from pkg_resources import to_filename
from gecko_api import GeckoApi

import datetime
import pytz
import json

def convert_date_time_to_string(date, hour, minute, period):
    if period == "PM":
        hour = hour + 12
    date_time_str = (str(date) + " " + str(hour) + ":" + str(minute))

    return date_time_str

def get_list_of_coins():
        data = json.load(open("market_cap_ranking_coin_list.json", encoding="utf8"))
        name_list = [item.get("name") for item in data]

        return name_list

class ManualTransaction:
    local_date_time = ""
    timezone = ""
    is_buy = True if 'buy' else False  # default value: True = Buy; False = Sell

    def __init__(self, id_num, crypto_name, buy_or_sell, price, num_coins_trading, target, fee, time):
        self.id = id_num
        self.crypto_name = crypto_name
        self.num_coins_trading = num_coins_trading  # amount
        self.fee = fee
        self.is_buy = buy_or_sell
        self.current_price = price
        self.trade_value = self.trade_value_format()
        self.target = target
        self.utc_date_time = time

    def return_transaction(self):
        """ Stores the transaction into a dictionary with a key where it's values is set to [date + time purchased:
        coin name, the amount] """
        key = str(str(self.utc_date_time) + ": " + self.crypto_name, self.num_coins_trading)
        transaction_dictonary = {}
        if key not in transaction_dictonary:
            transaction_dictonary[key] = {self.crypto_name, self.is_buy, self.current_price,
                                           self.num_coins_trading, self.target, self.utc_date_time}
        return transaction_dictonary

    def quantity_display(self):
        """
        This determines the net change and formats of coins for the transaction

        :rtype
        :return
        """
        if self.is_buy:
            return "\033[92m +{0:.1f}".format(self.num_coins_trading)
        else:
            return "\033[91m -{0:.1f}".format(self.num_coins_trading)

    def display_local(self):
        """
        Converts date time and timezone from UTC to the users local time zone
        Also formats local date and time to user friendly string

        :rtype = datetime str
        :return
        """
        local_datetime = self.utc_date_time.replace(tzinfo=pytz.utc)
        local_datetime = local_datetime.astimezone(tz=None)

        local_datetime_str = local_datetime.strftime("%b %d, %Y %H:%M %p")

        return local_datetime_str

    def trade_value_format(self):
        """
        returns the price value in USD of transaction
        calculates price by multiplying current_price and num_coins_trading

        :rtype str
        """
        return "${0:.2f}".format(self.current_price * self.num_coins_trading)

    def display_profit_loss(self, value):
        """
        returns the profit or loss value formatted as green or red if profit is positive
        or negative as a %

        :rtype str
        """
        if value >= 0:
            return "\033[92m +{0:.1f}%".format(value)
        else:
            return "\033[91m -{0:.1f}%".format(self.num_coins_trading)

    def display_holdings(self, value):
        """
        returns a string formatting the holdings value to one decimal place
        
        :rtype str
        """
        return "${0:.1f}".format(value)


# def main():
# #     users_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
# #     datetime.datetime.now()  # is the current time zone

# #     # print("key: " + str(date_time) + " " + "crypto_name", "num_coins_trading")
# #     utc_dt = datetime.datetime.utcnow()

# #     mt = ManualTransaction("Bitcoin", 2, 0, True)

# #     print("current UTC date and time: " + str(utc_dt))
# #     print("display_local() method: " + str(mt.display_local()))

# #     # print(str(dt))
# #     # print(users_timezone)

# #     # print("Formatted UTC datetime: " + str(utc_dt.strftime("%b %d %Y %X %p")))

#     name_list = get_list_of_coins()
#     print(name_list[0])


# if __name__ == "__main__":
#     main()
