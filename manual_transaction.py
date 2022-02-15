""" module that users inputs into a transaction """
from gecko_api import GeckoApi

import datetime
import pytz


class ManualTransaction:
    local_date_time = ""
    timezone = ""
    is_buy = True if 'buy' else False  # default value: True = Buy; False = Sell

    def __init__(self, crypto_name, num_coins_trading, fee, buy_or_sell):
        self.crypto_name = crypto_name
        self.num_coins_trading = num_coins_trading
        self.fee = fee
        self.is_buy = buy_or_sell

        self.current_price = GeckoApi(crypto_name).get_attribute("current_price")
        self.trade_value = self.trade_value_format()
        self.utc_date_time = datetime.datetime.utcnow()  # date time that will be stored
        self.timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        self.local_date_time = datetime.datetime.now()

    def return_transaction(self):
        """ Stores the transaction into a dictionary with a key where it's values is set to [date + time purchased:
        coin name, the amount] """
        key = str(str(self.utc_date_time) + ": " + self.crypto_name, self.num_coins_trading)
        transaction_dictonary = {}
        if key not in transaction_dictonary:
            transaction_dictonary[key] = {self.utc_date_time, self.timezone, self.crypto_name
                , self.num_coins_trading, self.trade_value, self.fee, self.is_buy}
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

    def to_local(self, utc_dt):
        """
        Converts timezones from UTC to the users local time zone

        :param utc_dt: datetime object
        :type utc_dt:
        :rtype = datetime obj
        :return
        """
        self.local_datetime = utc_dt.replace(tzinfo=pytz.utc)

        local_datetime = self.local_datetime.astimezone(tz=None)

        return local_datetime

    def trade_value_format(self):
        """
        returns the price value in USD of transaction
        calculates price by multiplying current_price and num_coins_trading

        :rtype float
        """
        return "${0:.2f}".format(self.current_price * self.num_coins_trading)


def main():
    users_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
    datetime.datetime.now()  # is the current time zone

    # print("key: " + str(date_time) + " " + "crypto_name", "num_coins_trading")
    utc_dt = datetime.datetime.utcnow()

    mt = ManualTransaction("Bitcoin", 2, 0, True)

    print("current UTC date and time: " + str(utc_dt))
    print("UTC to local conversion: " + str(mt.to_local(utc_dt)))

    # print(str(dt))
    print(users_timezone)


if __name__ == "__main__":
    main()
