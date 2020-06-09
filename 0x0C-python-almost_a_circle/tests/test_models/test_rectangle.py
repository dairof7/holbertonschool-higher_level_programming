#!/usr/bin/python3
"""
Unittests - Rectangle class
"""

import contextlib
import io
import unittest
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Rectangle test"""

    def setUp(self):
        """setup of unittes"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """delete existing files"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_11(self):
        """Test 16 to_dictionary method"""
        s1 = Rectangle(4, 5)
        s_dict = {'x': 0, 'width': 4, 'height': 5, 'y': 0, 'id': 1}
        self.assertDictEqual(s1.to_dictionary(), s_dict)
        self.assertEqual(s1.to_dictionary() is s_dict, False)
        s2 = Rectangle(4, 5, 5)
        s_dict = {'x': 5, 'width': 4, 'height': 5, 'y': 0, 'id': 2}
        self.assertDictEqual(s2.to_dictionary(), s_dict)
        self.assertEqual(s2.to_dictionary() is s_dict, False)
        s3 = Rectangle(4, 5, 5, 7)
        s_dict = {'x': 5, 'width': 4, 'height': 5, 'y': 7, 'id': 3}
        self.assertDictEqual(s3.to_dictionary(), s_dict)
        self.assertEqual(s3.to_dictionary() is s_dict, False)
        s4 = Rectangle(4, 5, 5, 7, 9)
        s_dict = {'x': 5, 'width': 4, 'height': 5, 'y': 7, 'id': 9}
        self.assertDictEqual(s4.to_dictionary(), s_dict)
        self.assertEqual(s4.to_dictionary() is s_dict, False)

    def test_12(self):
        """Test - to_json_string"""
        s1 = Rectangle(2, 6, 2)
        dictionary = s1.to_dictionary()
        json_d = Base.to_json_string([dictionary])
        self.assertEqual(type(json_d), str)
        self.assertDictEqual(
            dictionary, {'id': 1, 'x': 2, 'y': 0, 'width': 2, 'height': 6})

    def test_13(self):
        """Test - save_to_file method"""
        s1 = Rectangle(2, 6, 2)
        s2 = Rectangle(2, 4, 3, 6)
        Rectangle.save_to_file([s1, s2])
        res = '[{"x": 2, "y": 0, "width": 2, "height": 6, "id": 1},' + \
            ' {"x": 3, "y": 6, "width": 2, "height": 4, "id": 2}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_14(self):
        """Test - save_to_file - load_from_file method"""
        s1 = Rectangle(2, 6, 2, 8)
        Rectangle.save_to_file([s1])
        datafromfile = Rectangle.load_from_file()
        res = '[{"x": 2, "y": 0, "width": 2, "height": 6, "id": 1}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))
        string = ""
        for data in datafromfile:
            string += str(data)
        self.assertEqual(string, "[Rectangle] (1) 2/8 - 2/6")

    def test_15(self):
        """Test 20 load void"""
        sl = Rectangle.load_from_file()
        self.assertEqual(sl, [])

    def test_16(self):
        """Test """
        s1 = Rectangle(1, 25, 34, 7)
        s1_dict = s1.to_dictionary()
        s2 = Rectangle.create(**s1_dict)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_17(self):
        """Test - save_to_file None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_18(self):
        """Test - save_to_file []"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_20(self):
        """Test - display a Rectangle"""
        r = Rectangle(3, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        f6 = "###\n###\n###\n###\n###\n"
        self.assertEqual(s, f6)
        r = Rectangle(3, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        t = "###\n###\n###\n###\n"
        self.assertEqual(s, t)
        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "#\n"
        self.assertEqual(s, o)
