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

""" Returns the dictionary for a given coin. 
    Users must enter name (not symbol), not case-sensitive.
    @param name: name of coin
    @return coin: the queried coin dictionary"""
        
def get_coin(name):

    url_1 = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" 
    url_2 = "&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    coin = requests.get(url_1 + name.lower() + url_2).json()

    return coin
    

""" Returns a given attribute for a given coin.       
    Users must enter name (not symbol), not case-sensitive.
    @param attribute: the given attribute (use any from Attributes table above)
    @param name: name of coin
    @return the desired attribute for given coin"""
    
def get_attribute(name, attribute):
    
    coin = get_coin(name)
    if coin:
        return coin[0][attribute]

""" Returns an Image object representing the icon for a given coin.
    @param asset_id: coin identifier
    @return icon: the icon as an Image object"""

def get_icon(name): 
    
    coin = get_coin(name)
    if coin:
        url = coin[0]["image"]
        response = requests.get(url)
        image_bytes = BytesIO(response.content)
        icon = Image.open(image_bytes)
        return icon

"""  demonstration of the above methods """
# line_break = "----------------------------------------------"
    
# # get_coin method
# print("get_coin method to print ethereum dictionary\n" + line_break)
print(get_coin("vertcoin"))

# # get_attribute method
# print("\n\nget_attribute_method to print market cap for litecoin\n" + line_break)
# print(get_attribute("litecoin", "market_cap"))

# # get_icon method
# print("\n\nget_icon method to display icon for dogecoin\n" + line_break)
# get_icon("dogecoin").show()
