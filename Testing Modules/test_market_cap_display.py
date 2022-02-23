import unittest
from market_cap_display import MarketCapDisplay

class TestMarketCapCalculator(unittest.TestCase):
    
    def setUp(self):
        self.coin_1 = MarketCapDisplay("Bitcoin")
        self.coin_2 = MarketCapDisplay("Ethereum")    

    def tearDown(self):
        pass

    def test_display_market_cap(self):
        self.assertEqual(self.coin_1.display_market_cap(), "$738063232183.00")
        self.assertEqual(self.coin_2.display_market_cap(), "$326278354132.00")

    def test_display_market_cap(self):
        self.assertEqual(self.coin_1.display_market_cap_rank(), "2")
        self.assertEqual(self.coin_2.display_market_cap_rank(), "3")

if __name__ == '__main__':
    unittest.main()