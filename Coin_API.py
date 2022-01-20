# -*- coding: utf-8 -*-
"""
Author: Jessica Bidon
Date: Tues Jan 19, 2022
File: Coin_API.py

Description: This module connects to CoinAPI and captures information 
about over 13,000 different currencies, updated every 5 minutes.

Uncomment main (line 139) for a demonstration of the methods. 

CoinAPI documentation: https://docs.coinapi.io/#list-all-assets-get"""

""" TODO: 
        - create method to return list or file of all currency names/ids
            (for data cleaning/analysis)
        - integrate Coin_API with Coin_Icon_API?
        - create similar class for exchanges/symbols? 
            * https://docs.coinapi.io/#list-all-exchanges-get
            * https://docs.coinapi.io/#list-all-exchange-icons-get
            * https://docs.coinapi.io/#list-all-symbols-get
            
"""

# ========================================================================= #
#                              Attributes                                   # 
#  -----------------------------------------------------------------------  #
#   asset_id             |   asset identifier (ex. BTC for Bitcoin)         #
#   name                 |   name of coin                                   #
#   type_is_crypto       |   boolean value (1 for crypto, else 0)           #
#  ----------------------|------------------------------------------------  #
#   data_quote_start     |   date and time of the first quote               #
#   data_quote_end       |   date and time of the last quote                #
#  ----------------------|------------------------------------------------  #
#   data_orderbook_start |   date and time for first order book             #
#   data_orderbook_end   |   date and time for the last order book          #
#  ----------------------|------------------------------------------------  #
#   data_trade_start     |   date and time for first trade                  #
#   data_trade_end       |   data and time for the last trade               #
#  ----------------------|------------------------------------------------  #
#   data_symbols_count   |   number of symbols for given asset              #
#  ----------------------|------------------------------------------------  #
#   volume_1hrs_usd      |   USD volume of all symbols from last 1 hour     #
#                        |          rolling period                          #
#   volume_1day_usd      |   USD volume of all symbols from last 1 day      #
#                        |          rolling period                          #
#   volume_1mth_usd      |   USD volume of all symbols from last 1 month    #
#                        |          rolling period                          #
#  ----------------------|------------------------------------------------  #
#   price_usd            |   the actual USD price                           #
# ========================================================================= #

import requests

class Coin_API():

    """ Constructor connects to assets API"""
    def __init__(self):
        
        # url and headers for connecting
        url = 'https://rest.coinapi.io/v1/assets'
        headers = {'X-CoinAPI-Key' : '752B734A-A957-4648-8183-07B1DE32821A'}
        
        # assets is represented as a list of dictionaries, 
        # each containing info about a different coin
        self.assets = requests.get(url, headers=headers).json()

                ###             Methods             ###
    
    """ Returns the dictionary for a given coin. 
        Users may enter name or asset_id.
        @param name (optional): name of coin
        @param asset_id (optional): coin identifier
        @return coin: the queried coin dictionary"""
        
    def get_coin_dict(self, name="", asset_id=""):
        
        # initialize empty dictionary
        coin = {}
            
        # if user entered name
        if name != "":
            # strip whitespace, convert to lowercase to make searching consistent
            name = name.lower().strip()
            # the correct coin is the next one with given coin name, otherwise None
            coin = next((item for item in self.assets if item["name"].lower()==name), None)
        
        # if user entered asset_id, same logic as above
        elif asset_id != "":
            asset_id = asset_id.lower().strip()
            coin = next((item for item in self.assets if item["asset_id"].lower()==asset_id), None)

        return coin


    """ Returns a given attribute for a given coin. 
        Users may enter name or asset_id.        
        @param attribute: the given attribute (use any from Attributes table above)
        @param name (optional): name of coin
        @param asset_id (optional): coin identifier
        @return coin: the queried coin dictionary"""
        
    def get_attribute(self, attribute, name="", asset_id=""):
        
        coin = {}
        
        # get coin dictionary
        if name != "":
            coin = self.get_coin_dict(name=name)
        
        elif asset_id != "":
            coin = self.get_coin_dict(asset_id=asset_id)
            
        return coin[attribute]


    """ Returns the number of currencies captured by API.    
        @return size: the size of the currencies list"""
        
    def get_size(self):
        
        size = len(self.assets)
        return(size)
    
    
    """ Returns the number of cryptocurrencies captured by API.    
        @return count: the number of cryptocurrencies"""
        
    def count_crypto(self):
        
        count = 0
        for item in self.assets:
            if item["type_is_crypto"] == 1:
                count += 1
        return count
    
        
""" Demonstrates the various methods implemented in the Coin_API class. """   
# class Main():
    
#     line_break = "----------------------------------------------"
    
#     api = Coin_API()
    
#     # get_coin_dict method with coin name
#     print("get_coin_dict method using name to get Cardano dictionary\n" + line_break)
#     print(api.get_coin_dict(name="Cardano"))

#     # get_coin_dict method with coin id
#     print("\n\nget_coin_dict method using asset_id to get IOTA dictionary\n" + line_break)
#     print(api.get_coin_dict(asset_id="iota"))
    
#     # get attribute method
#     # note: any attribute on the Attributes table may be used, 
#     #           and either asset_id or name may be used
#     print("\n\nget_attribute_method to get current price of bitcoin\n" + line_break)
#     print(api.get_attribute("price_usd", asset_id="btc"))
    
#     # get size method and count_crypto methods
#     print("\n\nget_size and count_crypto methods\n" + line_break)
#     count = api.get_size()
#     crypto_count = api.count_crypto()
#     print("# of cryptocurrencies: " + str(crypto_count))
#     print("# of non-cryptocurrencies: " + str(count - crypto_count))
