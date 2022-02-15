import unittest
import weighted_calculator

class TestWeightedCalculator(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_weighted_calculator(self):
        weight_list = [10, 5, 24, 30, 7, 15]
        value_list = [12, 45, 2, 53, 23, 56]
        self.assertEqual(32.79, weighted_calculator.weighted_calculator(weight_list, value_list))

if __name__ == '__main__':
    unittest.main()