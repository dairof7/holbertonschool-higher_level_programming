#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for integers"""

    def test_max_integer(self):
        """Function to test sucefull cases
        positive and negative numbers
        """
        self.assertEqual(max_integer([-16, 27, 49]), 49)
        self.assertEqual(max_integer([2416, 327, 3, 49]), 2416)
        self.assertEqual(max_integer([0, -27, 1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1.5, 4, 5.6]), 5.6)


    def error_1(self):
        """Function to test error case
        when insert a char
        """
        with self.assertRaises(TypeError):
            max_integer([3, 4, "g"])

    def error_2(self):
        """Function to test error case
        when insert a boolean
        """
        with self.assertRaises(TypeError):
            max_integer([True, 4, 5])


if __name__ == '__main__':
    unittest.main()