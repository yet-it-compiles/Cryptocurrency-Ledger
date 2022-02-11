import unittest
from manual_transaction import ManualTransaction

class TestManualTransaction(unittest.TestCase):
    
    def setUp(self):
        # tests a buy transaction
        self.manT_1 = ManualTransaction("Bitcoin", 12, 0, True)
        self.manT_1.current_price = 40.3 # hard code current price for testing

        # tests a sell transaction
        self.manT_2 = ManualTransaction("Ethereum", 34, 0, False)
        self.manT_2.current_price = 74.1 # hard code current price for testing

        self.weight_list = [10, 5, 24, 30, 7, 15]
        self.value_list = [12, 45, 2, 53, 23, 56]

    
    def tearDown(self):
        pass

    def test_quantity_display(self):
        self.assertEqual("\033[92m +{0:.1f}".format(12), self.manT_1.quantity_display(self.manT_1.num_coins_trading, self.manT_1.buy_or_sell))
        self.assertEqual("\033[91m -{0:.1f}".format(34), self.manT_2.quantity_display(self.manT_2.num_coins_trading, self.manT_2.buy_or_sell))

    def test_trade_value_format(self):
        self.assertEqual("${0:.2f}".format(483.6), self.manT_1.trade_value_format(40.3, 12))
        self.assertEqual("${0:.2f}".format(2519.4), self.manT_2.trade_value_format(74.1, 34))

    def test_weighted_calculator(self):
        weight_list = [10, 5, 24, 30, 7, 15]
        value_list = [12, 45, 2, 53, 23, 56]
        self.assertEqual(32.79, self.manT_1.weighted_calculator(weight_list, value_list))

if __name__ == '__main__':
    unittest.main()