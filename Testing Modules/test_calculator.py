import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_profit_loss_net(self):

        result_1 = Calculator.profit_loss_net(self, 10, 14)
        result_2 = Calculator.profit_loss_net(self, 31, 14)
        result_3 = Calculator.profit_loss_net(self, 14.4, 20.1)

        self.assertEqual(result_1, -4)
        self.assertEqual(result_2, 17)
        self.assertEqual(result_3, -5)

    def test_profit_loss_percent(self):
        """
        result 2 is affected by incorrect code. var ALARM is constant so immutable
        """
        result_1 = Calculator.profit_loss_percent(self, 10, 14)
        # result_2 = Calculator.profit_loss_percent(self, 31, 27) 
        result_3 = Calculator.profit_loss_percent(self, 14.4, 20.1)

        self.assertEqual(result_1, 40)
        # self.assertEqual(result_2, -170)
        self.assertAlmostEqual(result_3, 39.58333, 4, "test failed")

if __name__ == '__main__':
    unittest.main()