#!/usr/bin/python3

"""
Unittest for Base class
"""
import pep8
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        """setup of unittest"""
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test - id int"""
        b0 = Base(8)
        b1 = Base(-7)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b0.id, 8)
        self.assertEqual(b1.id, -7)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()
