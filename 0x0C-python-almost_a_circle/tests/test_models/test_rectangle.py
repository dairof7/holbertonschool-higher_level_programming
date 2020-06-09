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

    def test_00(self):
        """Test - checking attributes"""
        s1 = Rectangle(4, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Rectangle(3, 4, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 4)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 0)
        s3 = Rectangle(3, 4, 5, 6)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 4)
        self.assertEqual(s3.x, 5)
        self.assertEqual(s3.y, 6)
        s4 = Rectangle(3, 4, 5, 6, 9)
        self.assertEqual(s4.id, 9)
        self.assertEqual(s4.width, 3)
        self.assertEqual(s4.height, 4)
        self.assertEqual(s4.x, 5)
        self.assertEqual(s4.y, 6)

    def test_01(self):
        """Test - non integer value"""
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(None, 5)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle((4, ), 5)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle("s", 6)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle(5.6, 7)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle([2, 3], 5)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, "df")
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, None)
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, (4, ))
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, [2, 3])
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Rectangle(5, 7.6)
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(1, 2, "s")
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(1, 3, 5.6)
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, 4, 4, "g")
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Rectangle(2, 4, 5, 5.6)
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        s1 = Rectangle(2, 3, 4, 5, "sdf")
        self.assertEqual(s1.id, "sdf")
        s2 = Rectangle(2, 3, 4, 6, False)
        self.assertEqual(s2.id, False)

    def test_03(self):
        """Test one argument"""
        with self.assertRaises(TypeError) as err:
            s = Rectangle(2)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(err.exception))

    def test_04(self):
        """Test - negative int"""
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(-2, -1)
        self.assertEqual(
            "width must be > 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(2, -1)
        self.assertEqual(
            "height must be > 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s2 = Rectangle(1, 4, -2)
        self.assertEqual(
            "x must be >= 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(1, 4, 2, -4)
        self.assertEqual(
            "y must be >= 0",
            str(err.exception))
        s1 = Rectangle(2, 3, 4, 5, -5)
        self.assertEqual(s1.id, -5)

    def test_04(self):
        """Test - zero values"""
        s1 = Rectangle(2, 1, 0, 0, 6)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 6)
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(0, 2, 3, 2)
        self.assertEqual(
            "width must be > 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(20, 0, 3, 2)
        self.assertEqual(
            "height must be > 0",
            str(err.exception))

    def test_05(self):
        """Test - Areas"""
        s1 = Rectangle(2, 6)
        self.assertEqual(s1.area(), 12)
        s1 = Rectangle(3, 3)
        self.assertEqual(s1.area(), 9)
        s1 = Rectangle(4, 3, 5)
        self.assertEqual(s1.area(), 12)
        s1 = Rectangle(5, 3, 6, 7)
        self.assertEqual(s1.area(), 15)

    def test_06(self):
        """Test - str"""
        s1 = Rectangle(2, 3)
        self.assertEqual(s1.__str__(), "[Rectangle] (1) 0/0 - 2/3")
        s1 = Rectangle(3, 4, 5)
        self.assertEqual(s1.__str__(), "[Rectangle] (2) 5/0 - 3/4")
        s1 = Rectangle(4, 3, 5, 6)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 5/6 - 4/3")
        s1 = Rectangle(5, 3, 6, 7, 8)
        self.assertEqual(s1.__str__(), "[Rectangle] (8) 6/7 - 5/3")

    def test_07(self):
        """Test - Update"""
        s1 = Rectangle(2, 2)
        self.assertEqual(s1.__str__(), "[Rectangle] (1) 0/0 - 2/2")
        s1.update(3, 3)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 0/0 - 3/2")
        s1.update(3, 3, 4)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 0/0 - 3/4")
        s1.update(3, 3, 4, 5)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 5/0 - 3/4")
        s1.update(3, 3, 4, 5, 9)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 5/9 - 3/4")

    def test_08(self):
        """Test - Update with names"""
        s1 = Rectangle(2, 3)
        self.assertEqual(s1.__str__(), "[Rectangle] (1) 0/0 - 2/3")
        s1.update(id=3)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 0/0 - 2/3")
        s1.update(height=4, id=3)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 0/0 - 2/4")
        s1.update(id=3, x=6, width=5)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 6/0 - 5/4")
        s1.update(y=7, id=3, x=6)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 6/7 - 5/4")
        s1.update(height=3)
        self.assertEqual(s1.__str__(), "[Rectangle] (3) 6/7 - 5/3")

    def test_09(self):
        """Test - unknowm attribute"""
        s1 = Rectangle(2, 5)
        s1.update(hi=3)
        self.assertEqual(hasattr(s1, 'hi'), False)

    def test_10(self):
        """Test mod atribute by assignment"""
        s1 = Rectangle(12, 4)
        self.assertEqual(s1.width, 12)
        s1.width = 25
        self.assertEqual(s1.width, 25)
        s1.height = 5
        self.assertEqual(s1.height, 5)
        with self.assertRaises(TypeError) as err:
            s1.width = "asdasd"
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.width = [44, 56]
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.width = True
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.width = {"aasd": 5}
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.width = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.width = (5,)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))

        with self.assertRaises(TypeError) as err:
            s1.height = "asdasd"
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.height = [44, 56]
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.height = True
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.height = {"aasd": 5}
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.height = {1, 2}
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.height = (5,)
        self.assertEqual(
            "height must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.x = "asdasd"
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.x = [44, 56]
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.y = True
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.y = {"aasd": 5}
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.x = {1, 2}
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.y = (5,)
        self.assertEqual(
            "y must be an integer",
            str(err.exception))

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
