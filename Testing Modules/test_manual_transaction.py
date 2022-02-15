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
    
    def tearDown(self):
        pass

    def test_quantity_display(self):
        self.assertEqual("\033[92m +{0:.1f}".format(12), self.manT_1.quantity_display())
        self.assertEqual("\033[91m -{0:.1f}".format(34), self.manT_2.quantity_display())

    def test_trade_value_format(self):
        self.assertEqual("${0:.2f}".format(483.6), self.manT_1.trade_value_format())
        self.assertEqual("${0:.2f}".format(2519.4), self.manT_2.trade_value_format())

if __name__ == '__main__':
    unittest.main()
