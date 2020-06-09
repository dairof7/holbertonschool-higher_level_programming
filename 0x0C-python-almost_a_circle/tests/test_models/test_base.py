#!/usr/bin/python3

"""
Unittest for Base class
"""

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


if __name__ == '__main__':
    unittest.main()
