import unittest
from percent_change_calculator import PercentChange

class TestPercentChange(unittest.TestCase):

    def setUp(self):
            self.price_1 = PercentChange(120, 112) 
            self.price_2 = PercentChange(120, 137) 
            self.price_3 = PercentChange(-1, 2) 

    def tearDown(self):
        pass
    
    def test_percent_increase(self):
        self.assertAlmostEqual(float(self.price_1.percent_increase()), -6.66667, 2, "error when there is a negative percent change")
        self.assertAlmostEqual(float(self.price_2.percent_increase()), 14.16667, 2, "error when there is a postive percent change")
        self.assertAlmostEqual(float(self.price_3.percent_increase()), 300, 2, "error when there is a sign change")

    def test_price_difference(self):
        self.assertEqual(self.price_1.price_difference(), 8)
        self.assertEqual(self.price_2.price_difference(), 17)

if __name__ == '__main__':
    unittest.main()