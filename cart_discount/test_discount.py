import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario


    def test_discount_with_float_value(self):
        prices = [50.0, 4.6, 45.5]
        expected_discount = 4.6
        self.assertEqual(expected_discount, discount(prices))

    def test_list_smaller_thatn_three(self):
        prices = [10, 4]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

    def test_string_in_list(self):
        items = ['string',  'lists', 'string']
        expected_discount = None
        value_return = discount(items)
        self.assertEqual(expected_discount, value_return)

    def test_larger_than_three(self):
        prices = [45, 6, 4, 65, 65, 34, 23, 12, 32, 43, 54, 65 ,76, 87, 98, 21, 34, 26, 58]
        expected_discount = 4
        self.assertAlmostEqual(expected_discount, discount(prices))

    def test_list_2_prices(self):
        prices = [32, 43]
        expected_discount = None
        self.assertAlmostEqual(expected_discount, discount(prices))





if __name__ == '__main__':
    unittest.main()