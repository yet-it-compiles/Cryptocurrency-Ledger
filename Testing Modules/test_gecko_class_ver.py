import unittest
import requests
from PIL import Image
from io import BytesIO
from gecko_api import GeckoApi

class TestGeckoApi(unittest.TestCase):
    
    def setUp(self):
        self.coin_1 = GeckoApi("Tether")
        self.coin_2 = GeckoApi("Ethereum")
        # tests for unexisting cryptocurrency
        self.coin_3 = GeckoApi("FakeCoin")

    def tearDown(self):
        pass

    def test_get_attribute(self):
        self.assertEqual(self.coin_1.get_attribute("symbol"), "usdt")
        self.assertEqual(self.coin_2.get_attribute("symbol"), "eth")

    def test_get_ohlc_data(self):
        self.emptyLst = []
        self.assertCountEqual(self.coin_3.get_ohlc_data(4), self.emptyLst)

if __name__ == '__main__':
    unittest.main()