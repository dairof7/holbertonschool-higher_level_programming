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

    def test_load_from_file(self):
        """test_load_from_file test classmethod output"""

        Base_Base__nb_objects = 0
        R1 = Rectangle(4, 7)
        R2 = Rectangle(6, 9)
        R1_d = R1.to_dictionary()
        R2_d = R2.to_dictionary()
        list_obj = [R1, R2]
        Rectangle.save_to_file(list_obj)
        list_instances = Rectangle.load_from_file()

        self.assertIsInstance(list_instances[0], Rectangle)
        self.assertIsInstance(list_instances[1], Rectangle)

        self.assertDictEqual(list_instances[0].to_dictionary(), R1_d)
        self.assertDictEqual(list_instances[1].to_dictionary(), R2_d)