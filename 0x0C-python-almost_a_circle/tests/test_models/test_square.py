#!/usr/bin/python3
"""
Unittests - Square class
"""

import io
import unittest
import sys
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class TestSquare(unittest.TestCase):
    """Test square"""
    def setUp(self):
        """steup of unittes"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """deleting files if exist"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_11(self):
        """Test 16 to_dictionary method"""
        s1 = Square(4)
        s_dict = {'x': 0, 'size': 4, 'y': 0, 'id': 1}
        self.assertDictEqual(s1.to_dictionary(), s_dict)
        self.assertEqual(s1.to_dictionary() is s_dict, False)
        s2 = Square(4, 5)
        s_dict = {'x': 5, 'size': 4, 'y': 0, 'id': 2}
        self.assertDictEqual(s2.to_dictionary(), s_dict)
        self.assertEqual(s2.to_dictionary() is s_dict, False)
        s3 = Square(4, 5, 7)
        s_dict = {'x': 5, 'size': 4, 'y': 7, 'id': 3}
        self.assertDictEqual(s3.to_dictionary(), s_dict)
        self.assertEqual(s3.to_dictionary() is s_dict, False)
        s4 = Square(4, 5, 7, 9)
        s_dict = {'x': 5, 'size': 4, 'y': 7, 'id': 9}
        self.assertDictEqual(s4.to_dictionary(), s_dict)
        self.assertEqual(s4.to_dictionary() is s_dict, False)

    def test_12(self):
        """Test - to_json_string"""
        s1 = Square(2, 6, 2)
        dictionary = s1.to_dictionary()
        json_d = Base.to_json_string([dictionary])
        self.assertEqual(type(json_d), str)
        self.assertDictEqual(dictionary, {'id': 1, 'x': 6, 'y': 2, 'size': 2})

    def test_13(self):
        """Test - save_to_file method"""
        s1 = Square(2, 6, 2)
        s2 = Square(2, 4, 3, 6)
        Square.save_to_file([s1, s2])
        res = '[{"x": 6, "y": 2, "size": 2, "id": 1},' + \
            ' {"x": 4, "y": 3, "size": 2, "id": 6}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_15(self):
        """Test 20 load void"""
        sl = Square.load_from_file()
        self.assertEqual(sl, [])

    def test_16(self):
        """Test """
        s1 = Square(1, 25, 34, 7)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_17(self):
        """Test - save_to_file None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_18(self):
        """Test - save_to_file []"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_19(self):
        """Test compare instances"""
        s1 = Square(1, 2)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s1, Rectangle)
