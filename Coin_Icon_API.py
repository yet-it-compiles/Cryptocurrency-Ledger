# -*- coding: utf-8 -*-
"""
Author: Jessica Bidon
Date: Tues Jan 19, 2022
File: Coin_Icons_API.py

Description: This module connects to CoinAPI and captures links to icons 
for 2,820 different currencies. 

Uncomment main (line 85) for a demonstration of the methods. 

CoinAPI documentation: https://docs.coinapi.io/#list-all-asset-icons-get"""

""" TODO: 
        - get 
"""

# ========================================================================= #
#                              Attributes                                   # 
#  -----------------------------------------------------------------------  #
#   asset_id       |        asset identifier (ex. BTC for Bitcoin)          #
#   url            |        url linking to png of icon                      #
# ========================================================================= #

import requests
from PIL import Image
from io import BytesIO

class Coin_Icon_API():   

    
    """ Constructor connects to icons API """
    def __init__(self):

        # url and headers for connecting
        url = 'https://rest.coinapi.io/v1/assets/icons/{iconSize}'
        headers = {'X-CoinAPI-Key' : '752B734A-A957-4648-8183-07B1DE32821A'}
        
        # icons is represented as a list of dictionaries, 
        # each containing a coin name and url for it's icon
        self.icons = requests.get(url, headers=headers).json()
        
                ###             Methods             ###
        
    """ Returns the icon dictionary for a given coin. 
        @param asset_id: coin identifier
        @return coin: the queried dictionary"""        
        
    def get_icon_dict(self, asset_id):
        
        # strip whitespace, convert to lowercase to make searching consistent
        asset_id = asset_id.lower().strip()
        # the correct coin is the next one with the given id, otherwise None
        coin = next((item for item in self.icons if item["asset_id"].lower()==asset_id), None)
        
        return coin            
    
    
    """ Returns an Image object representing the icon for a given coin.
        @param asset_id: coin identifier
        @return icon: the icon as an Image object"""
        
    def get_icon(self, asset_id):
        
        # get url from dictionary, convert to Image
        url = self.get_icon_dict(asset_id)["url"]
        response = requests.get(url)
        image_bytes = BytesIO(response.content)
        icon = Image.open(image_bytes)
        
        return icon

    
    """ Returns the number of icons captured by API.
        @return size: the size of the icon list"""

    def get_size(self):
        size = len(self.icons)
        return(size)
    
    
    
    
""" Demonstrates the various methods implemented in the Coin_Icon_API class. """   
# class Main():
    
#     line_break = "----------------------------------------------"
    
#     api = Coin_Icon_API()
    
#     # get_icon_dict method
#     print("get_icon_dict method to get Vertcoin icon dictionary\n" + line_break)
#     print(api.get_icon_dict("vTC"))

#     # get size method
#     print("\n\nget_size method to get number of icons\n" + line_break)
#     print(api.get_size())
    
#     # get_icon method (returns Image)
#     print("\n\nget_icon method to show Litecoin icon\n" + line_break)
#     api.get_icon("LTc").show()