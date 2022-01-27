# -*- coding: utf-8 -*-
"""
Author: Jessica Bidon
Date: Thurs Jan 21, 2022
File: gecko_api.py
Description: This module connects to the CoinGecko API 
and captures information about different cryptocurrencies.
CoinGecko documentation: https://www.coingecko.com/en/api/documentation"""

# =================================================================================== #
#                                     Attributes                                      #
#  ---------------------------------------------------------------------------------  #
#   id                           |   name of coin for making API calls (ex. bitcoin)  #
#   symbol                       |   symbol of coin (ex. btc)                         #
#   name                         |   name of coin (ex. Bitcoin)                       #
#   image                        |   icon url                                         #
#  ------------------------------|--------------------------------------------------  #
#   current_price                |   latest trading price                             #
#   market_cap                   |   latest trading price x circulating supply        #
#   market_cap_rank              |   coin gecko rank based on market cap              #
#   fully_diluted_valuation      |   total value of market if all future coins exist  #
#   total_volume                 |   approx. # of coins that currently exist          #
#  ------------------------------|--------------------------------------------------  #
#   high_24h                     |   highest trading price in last 24 hours           #
#   low_24h                      |   lowest trading price in last 24 hours            #
#  ------------------------------|--------------------------------------------------  #
#   price_change_24h             |   price change since 24 hours ago                  #
#   price_change_percentage_24h  |   % price change since 24 hours ago                #
#   market_cap_change_24h        |   market cap change since 24 hours ago             #
#   market_cap_change_percentage |   $ market cap change since 24 hours ago           #
#  ------------------------------|--------------------------------------------------  #
#   circulating_supply           |   approx. # of coins currently in circulation      #
#   total_supply                 |   approx. # of coins that currently exist          #
#   max_supply                   |   approx. # of coins that will ever exist          #
#  ------------------------------|--------------------------------------------------  #
#   ath                          |   all-time high trading price                      #
#   ath_change_percentage        |   % change in all-time high vs. current price      #
#   ath_date                     |   date of all-time high trading price              #
#  ------------------------------|--------------------------------------------------  #
#   atl                          |   all-time low trading price                       #
#   atl_change_percentage        |   % change in all-time low vs. current price       #
#   atl_date                     |   date of all-time low trading price               #
#  ------------------------------|--------------------------------------------------  #
#   roi                          |   return on investment? specifics unclear          #
#   last_updated                 |   date/time when information was updated           #
# =================================================================================== #

import requests
from PIL import Image
from io import BytesIO


        
def get_coin(name):
    """ Returns the dictionary for a given coin. 
    Users must enter name (not symbol), not case-sensitive.
    :param name: name of coin
    :type name: str
    :rtype: dict
    :return coin: the queried coin dictionary"""

    url_1 = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" 
    url_2 = "&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    coin = requests.get(url_1 + name.lower().strip() + url_2).json()

    return coin
    

def get_attribute(name, attribute):
    """ Returns a given attribute for a given coin.       
    Users must enter name (not symbol), not case-sensitive.
    :param attribute: the given attribute (use any from Attributes table above)
    :type attribute: str
    :param name: name of coin
    :type name: str
    :rtype: int | float | str
    :return: the desired attribute for given coin"""
    
    coin = get_coin(name)
    if coin:
        return coin[0][attribute]
    
    
def get_ohlc(name, num_days_ago):
    """ Returns a list of ohlc data, each entry having the form:
            [unix_timestamp, open_price, high_price, low_price, close_price]
    Users enter the name of the coin (not symbol), not case-sensitive, 
    as well as the date range (from num_days_ago to current).
    The candlestick interval depends on the value of num_days_ago:
        <= 2 days ago: 30 minutes
        3-30 days ago: 4 hours
        >= 31 days ago: 4 days
    :param name: name of coin
    :type name: str
    :param num_days_ago: beginning of date range for ohlc data
    :type num_days_ago: int
    :rtype: list
    :return coin_ohlc: the coin's ohlc data for the past [num_days_ago] days
                        (empty list if coin does not exist)"""
   
    url_1 = 'https://api.coingecko.com/api/v3/coins/'
    url_2 = '/ohlc?vs_currency=usd&days='
    
   
    coin_ohlc = requests.get(url_1 + name.lower().strip() + url_2 + str(num_days_ago)).json()
    
    # return an empty list if the coin does not exist (api returns error dictionary)
    if type(coin_ohlc) == dict:
        coin_ohlc = []
    
    return coin_ohlc


def get_price_hist(name, num_days_ago, separate=False):
    """ Returns a list of historical price data, each entry having the form: 
            [unix_timestamp, price]
    Users enter the name of the coin (not symbol), not case_sensitive,
    as well as the date range (from num_days_ago to current).
    If the coin name is not recognized, any lists will return empty. 
    The interval depends on the value of num_days_ago:
        <= 1 day: minutely data
        1-90 days: hourly data
        >= 90 days: daily data
    :param name: name of coin
    :type name: str
    :param num_days_ago: beginning of date range for price history data
    :type num_days ago: int
    :param separate: if True, will separate the lists into two separate lists, times and prices
    :type separate: bool
    :rtype: list (if separate) | tuple of lists (times, prices)
    :return price_hist (a single list) | two separate lists, (times, prices)"""
    
    url_1 = 'https://api.coingecko.com/api/v3/coins/'
    url_2 = '/market_chart?vs_currency=usd&days='
    price_hist = requests.get(url_1 + name.lower().strip() + url_2 + str(num_days_ago)).json()
    
    # return empty list if coin name is not recognized
    if "error" in price_hist.keys():
        price_hist = []
    else:
        price_hist = price_hist["prices"]
    
    # separate json dictionary into two lists
    if separate:
        times = []
        prices = []
        # only try to split if price_hist is non-empty
        if price_hist:
            for item in price_hist:
                times.append(item[0])
                prices.append(item[1])
        return (times, prices)
    else:
        return price_hist
    
    
def get_market_cap_hist(name, num_days_ago, separate=False):
    """ Returns a list of historical market cap data, each entry having the form: 
            [unix_timestamp, market_cap]
    Users enter the name of the coin (not symbol), not case_sensitive,
    as well as the date range (from num_days_ago to current).
    If the coin name is not recognized, any lists will return empty. 
    The interval depends on the value of num_days_ago:
        <= 1 day: minutely data
        1-90 days: hourly data
        >= 90 days: daily data
    :param name: name of coin
    :type name: str
    :param num_days_ago: beginning of date range for market cap history data
    :type num_days ago: int
    :param separate: if True, will separate the lists into two separate lists, times and market_caps
    :type separate: bool
    :rtype: list (if separate) | tuple of lists (times, market_caps)
    :return market_caps_hist (a single list) | two separate lists, (times, market_caps)"""
    
    url_1 = 'https://api.coingecko.com/api/v3/coins/'
    url_2 = '/market_chart?vs_currency=usd&days='
    market_cap_hist = requests.get(url_1 + name.lower().strip() + url_2 + str(num_days_ago)).json()
    
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
            for item in market_cap_hist:
                times.append(item[0])
                market_caps.append(item[1])
        return (times, market_caps)
    else:
        return market_cap_hist


def get_volume_hist(name, num_days_ago, separate=False):
    """ Returns a list of historical total volume data, each entry having the form: 
            [unix_timestamp, total_volume]
    Users enter the name of the coin (not symbol), not case_sensitive,
    as well as the date range (from num_days_ago to current).
    If the coin name is not recognized, any lists will return empty. 
    The interval depends on the value of num_days_ago:
        <= 1 day: minutely data
        1-90 days: hourly data
        >= 90 days: daily data
    :param name: name of coin
    :type name: str
    :param num_days_ago: beginning of date range for total volume history data
    :type num_days ago: int
    :param separate: if True, will separate the lists into two separate lists, times and total_volumes
    :type separate: bool
    :rtype: list (if separate) | tuple of lists (times, total_volumes)
    :return total_volumes_hist (a single list) | two separate lists, (times, total_volumes)"""
    
    url_1 = 'https://api.coingecko.com/api/v3/coins/'
    url_2 = '/market_chart?vs_currency=usd&days='
    total_volume_hist = requests.get(url_1 + name.lower().strip() + url_2 + str(num_days_ago)).json()
        
    # return empty list if coin name is not recognized
    if "error" in total_volume_hist.keys():
        total_volume_hist = []
    else:
        total_volume_hist = total_volume_hist["total_volumes"]
    
    if separate:
        times = []
        total_volumes = []
        # only try to split if total_volume_hist is non-empty
        if total_volume_hist:
            for item in total_volume_hist:
                times.append(item[0])
                total_volumes.append(item[1])
        return (times, total_volumes)
    else:
        return total_volume_hist


def get_icon(name): 
    """ Returns an Image object representing the icon for a given coin.
    :param name: name of coin 
    :type name: str
    :rtype: Image
    :return icon: the icon as an Image object"""

    coin = get_coin(name)
    if coin:
        url = coin[0]["image"]
        response = requests.get(url)
        image_bytes = BytesIO(response.content)
        icon = Image.open(image_bytes)
        return icon


"""  demonstration of the above methods """
line_break = "----------------------------------------------"
    
# # get_coin method
# print("get_coin method to print ethereum dictionary\n" + line_break)
# print(get_coin("ethereum"))

# # get_attribute method
# print("\n\nget_attribute_method to print market cap for litecoin\n" + line_break)
# print(get_attribute("litecoin", "market_cap"))

# # get_ohlc method
# print("\n\nget_ohlc method to print last 30 days ohlc data for cardano (first 10 entries only)\n" + line_break)
# ohlc = get_ohlc("cardano", 30)
# # verify that list is non-empty before indexing (a misspelled/nonexistent coin will return an empty list)
# if ohlc:
#     print(ohlc[:10])

# # get_price_hist method (get_market_cap_hist() and get_total_volume_hist() work exactly the same way)
# print("\n\nget_price_hist method to print last 14 days historical data for polkadot,")
# print("without using 'separate' parameter (first 10 entries only)\n" + line_break)
# price = get_price_hist("polkadot", 14)
# # verify that list is non-empty before indexing (a misspelled/nonexistent coin will return an empty list)
# if price:
#     print(price[:10])

# # get_price_hist method (using the separate parameter to return the tuple of lists (times, prices))
# print("\n\nget_price_hist method to print last 14 days historical data for polkadot,")
# print("using the 'separate' parameter to split data into two lists, (times, prices) (first 10 entries only)\n" + line_break)
# price_hist = get_price_hist("polkadot", 14, separate=True)
# # verify that list is non-empty before indexing (a misspelled/nonexistent coin will return an empty list)
# if price_hist:
#     print("TIMES: ", price_hist[0][:10])
#     print("PRICES: ", price_hist[1][:10])

# # get_icon method
# print("\n\nget_icon method to display icon for dogecoin\n" + line_break)
# get_icon("dogecoin").show()
