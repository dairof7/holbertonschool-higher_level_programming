#!/usr/bin/python3
"""
Unittests - Square class
"""

import io
import unittest
import sys
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):


    def setUp(self):
        Base._Base__nb_objects = 0