""" Simple module which retrieves the requested cryptocurrency information """

import requests
from PIL import Image
from io import BytesIO


class GeckoApi:
    crypto_name = ""
    current_price = -1
    market_cap = -1
    total_volume = -1
    daily_high = -1
    daily_low = -1

    def __init__(self, crypto_name):
        self.name = crypto_name

    def get_coin(self):
        """
        Returns the dictionary representation of the coin with all available attributes

        :rtype: dict
        :return coin: the queried coin dictionary
        """
        info_from_api = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids="
        jason_converter = "&order=market_cap_desc&per_page=100&page=1&sparkline=false"
        requested_crypto_info = requests.get(info_from_api + self.name.lower() + jason_converter).json()

        return requested_crypto_info

    def get_attribute(self, attribute):
        """
        Retrieves a specific attribute request

        Note: Users must enter name (not symbol), not case-sensitive.

        :param attribute: the given attribute (use any from Attributes table above)
        :type attribute: str
        :rtype: int | float | str
        :return: the desired attribute for given coin
        """
        crypto_attribute = self.get_coin()
        if crypto_attribute:
            return crypto_attribute[0][attribute]

    def get_icon(self):
        """
        Retrieves the image of the requested cryptocurrency

        :rtype: Image
        :return icon: the icon as an Image object
        """

        crypto_image = self.get_coin()

        if crypto_image:
            crypto_image_url = crypto_image[0]["image"]  # captures the
            server_response = requests.get(crypto_image_url)
            image_bytes = BytesIO(server_response.content)
            crypto_icon = Image.open(image_bytes)
            return crypto_icon
        