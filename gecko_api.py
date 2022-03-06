""" Simple module which retrieves the requested cryptocurrency information """

import pandas as pd
import urllib.error
import requests
import json
from PIL import Image
from io import BytesIO


class GeckoApi:
    def __init__(self, crypto_name):
        cryptocurrency_name = crypto_name.lower().strip()

        with open("coins.json") as file:
            collection_of_coins = json.load(file)

            if collection_of_coins.get(cryptocurrency_name):
                if type(collection_of_coins[cryptocurrency_name]) == list:
                    self.name = collection_of_coins[cryptocurrency_name][0]
                else:
                    self.name = collection_of_coins[cryptocurrency_name]

    def get_coin(self):
        """
        Returns the dictionary representation of the coin with all available attributes

        :rtype: dict
        :return requested_crypto_info: the queried coin dictionary
        """
        if self.name:
            info_from_api = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids="
            json_converter = "&order=market_cap_desc&per_page=100&page=1&sparkline=false"
            requested_crypto_info = requests.get(info_from_api + self.name + json_converter).json()

            return requested_crypto_info[0]

    def get_attribute(self, attribute):
        """
        Retrieves a specific attribute request

        Note: Users must enter name (not symbol), not case-sensitive.

        :param attribute: the given attribute (use any from Attributes table above)
        :type attribute: str
        :rtype: int | float | str
        :return: crypto_attribute[0][attribute]
        """
        crypto_attribute = self.get_coin()

        if crypto_attribute:
            return crypto_attribute[attribute]

    def get_icon(self):
        """
        Retrieves the image of the requested cryptocurrency

        :rtype: Image
        :return crypto_icon
        """
        crypto_image = self.get_coin()

        if crypto_image:
            crypto_image_url = crypto_image["image"]
            server_response = requests.get(crypto_image_url)
            image_bytes = BytesIO(server_response.content)
            crypto_icon = Image.open(image_bytes)
            return crypto_icon

    def get_ohlc_data(self, days_previous):
        """
        Returns a list of opening price, high/low, and closing price for the period

        :param days_previous: int
        :rtype: list
        :return: coin_ohlc
        """
        api_url_1 = 'https://api.coingecko.com/api/v3/coins/'
        api_url_2 = '/ohlc?vs_currency=usd&days='

        # handle any days_previous input (API only accepts listed values below)
        possible_days = [1, 7, 14, 30, 90, 180, 365]
        if days_previous < 1:
            days_previous = 1
        elif days_previous not in possible_days:
            for days in enumerate(possible_days):
                if days_previous < days[1]:
                    days_previous = possible_days[days[0] - 1]
                    break
            else:
                days_previous = possible_days[-1]

        # Logic to fetch cryptocurrency data
        try:
            coin_ohlc = pd.read_json(api_url_1 + self.name + api_url_2 + str(days_previous))
            coin_ohlc.columns = ['date', 'open', 'high', 'low', 'close']
            coin_ohlc['date'] = pd.to_datetime(coin_ohlc['date'], unit='ms')
            coin_ohlc['date'] = pd.DatetimeIndex(coin_ohlc['date'])
            coin_ohlc = coin_ohlc.set_index('date')

        except urllib.error.HTTPError:
            coin_ohlc = []

        return coin_ohlc

    def get_price_history(self, days_previous, separate=False):
        """
        Returns a list of historical price data in the form of  [unix_timestamp, price]

        :param days_previous: int
        :param separate: bool
        :rtype: list
        :return: price_history
        """
        info_from_api = 'https://api.coingecko.com/api/v3/coins/'
        json_converter = '/market_chart?vs_currency=usd&days='
        price_history = requests.get(
            info_from_api + self.name + json_converter + str(days_previous)).json()

        # return empty list if coin name is not recognized
        if "error" in price_history.keys():
            price_history = []
        else:
            price_history = price_history["prices"]

        # Separates the json dictionary into two lists
        if separate:
            times = []
            prices = []

            # Attempts to split only if price_history is not empty
            if price_history:
                for each_element in price_history:
                    times.append(each_element[0])
                    prices.append(each_element[1])
            return times, prices
        else:
            return price_history

    def get_market_cap_history(self, days_previous, separate=False):
        """
        Returns a list of historical market cap data, each entry having the form: [unix_timestamp, market_cap]

        :param days_previous: int
        :param separate: bool
        :rtype: list
        :return: market_cap_hist
        """
        info_from_api = 'https://api.coingecko.com/api/v3/coins/'
        json_converter = '/market_chart?vs_currency=usd&days='
        market_cap_hist = requests.get(info_from_api + self.name + json_converter +
                                       str(days_previous)).json()

        # return empty list if coin name is not recognized
        if "error" in market_cap_hist.keys():
            market_cap_hist = []
        else:
            market_cap_hist = market_cap_hist["market_caps"]

        if separate:
            times = []
            market_caps = []
            # only try to split if market_cap_hist is non-empty
            if market_cap_hist:
                for each_item in market_cap_hist:
                    times.append(each_item[0])
                    market_caps.append(each_item[1])
            return times, market_caps
        else:
            return market_cap_hist

    def get_volume_history(self, days_previous, separate=False):
        """
        Returns a list of historical total volume data, each entry having the form: [unix_timestamp, total_volume]

        :param days_previous: int
        :param separate: bool
        :rtype: list
        :return: total_volume_history
        """
        info_from_api = 'https://api.coingecko.com/api/v3/coins/'
        json_converter = '/market_chart?vs_currency=usd&days='
        total_volume_history = requests.get(info_from_api, self.name, json_converter,
                                            str(days_previous)).json()

        # return empty list if coin name is not recognized
        if "error" in total_volume_history.keys():
            total_volume_history = []
        else:
            total_volume_history = total_volume_history["total_volumes"]

        if separate:
            times = []
            total_volumes = []
            # only try to split if total_volume_hist is non-empty
            if total_volume_history:
                for each_item in total_volume_history:
                    times.append(each_item[0])
                    total_volumes.append(each_item[1])
            return times, total_volumes
        else:
            return total_volume_history

    @staticmethod
    def get_prices(coins: list, ascending=False):
        """
        Takes a list of coins, and returns a dictionary of each with their respective prices from greatest to least

        Note: use coin name, not symbol (i.e. "bitcoin", not "btc")

        :param coins: list of coin names as strings
        :param ascending: determines sort order (default False)
        :rtype: dict
        :return: sort_dict | {}
        """
        if coins:
            # Logic to format the request
            api_url_1 = "https://api.coingecko.com/api/v3/simple/price?ids="
            api_url_2 = "&vs_currencies=usd"
            coins_str = ""

            for each_coin in coins[:-1]:  # starts from the end of the list
                coins_str = coins_str + each_coin + "%2c"
            coins_str = coins_str + coins[-1]

            # Logic to fetch data
            request = requests.get(api_url_1 + coins_str + api_url_2).json()

            # format data
            for each_coin in request.keys():
                request[each_coin] = request[each_coin]["usd"]

            if ascending:
                sort_coins = sorted(request.items(), key=lambda x: x[1])
            else:
                sort_coins = sorted(request.items(), key=lambda x: x[1], reverse=True)

            sorted_dictionary = {}
            for each_coin in sort_coins:
                sorted_dictionary[each_coin[0]] = each_coin[1]
            return sorted_dictionary
        else:
            return {}


def main():
    crypto_info = GeckoApi("bitcoin")

    # print('Cryptocurrency Name: ' + str(crypto_info.name).title())
    # print('Current Price: ' + str(crypto_info.get_attribute("current_price")))
    # print('Market Cap: ' + str(crypto_info.get_attribute("market_cap")))
    # print('Total Supply: ' + str(crypto_info.get_attribute("total_supply")))
    # print('Price High: ' + str(crypto_info.get_attribute("high_24h")))
    # print('Price Low: ' + str(crypto_info.get_attribute("low_24h")))
    # print('OHLC Data: ' + str(crypto_info.get_ohlc_data(2)))

    # print('Price History: ' + str(crypto_info.get_price_history(2)))
    # print('Market Cap History: ' + str(crypto_info.get_market_cap_history(2)))

    crypto_info.get_icon().show()

    prices = GeckoApi.get_prices(["shiba-inu", "bitcoin", "polkadot", "cardano", "dogecoin", "ethereum", "tether"])
    print(prices)


if __name__ == '__main__':
    main()
