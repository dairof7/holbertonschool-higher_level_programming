#!/usr/bin/python3
"""
Unittests - Rectangle class
"""

import io
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestRectangle(unittest.TestCase):


    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
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
            s1 = Rectangle([2,3], 5)
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
            s1 = Rectangle(2, [2,3])
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

    def test_02(self):
        """Test none argument"""
        with self.assertRaises(TypeError) as err:
            s = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(err.exception))


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
        s1=Rectangle(2, 6)
        self.assertEqual(s1.area(), 12)
        s1=Rectangle(3, 3)
        self.assertEqual(s1.area(), 9)
        s1=Rectangle(4, 3, 5)
        self.assertEqual(s1.area(), 12)
        s1=Rectangle(5, 3, 6, 7)
        self.assertEqual(s1.area(), 15)







    def test_19(self):
        """Test compare instances"""
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Base)
        self.assertIsInstance(r1, Rectangle)
        self.assertNotIsInstance(r1, Square)
