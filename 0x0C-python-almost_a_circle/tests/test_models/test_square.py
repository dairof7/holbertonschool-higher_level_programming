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

    def test_00(self):
        """Test - checking attributes"""
        s1 = Square(8)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, 8)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(4, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.width, 4)
        self.assertEqual(s2.height, 4)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        s3 = Square(3, 4, 5, 6)
        self.assertEqual(s3.id, 6)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 3)
        self.assertEqual(s3.x, 4)
        self.assertEqual(s3.y, 5)

    def test_01(self):
        """Test - non integer value"""
        with self.assertRaises(TypeError) as err:
            s1 = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Square("s")
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s2 = Square(5.6)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Square([2, 3])
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Square(1, "s")
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Square(1, 5.6)
        self.assertEqual(
            "x must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Square(2, 4, "g")
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1 = Square(2, 4, 5.6)
        self.assertEqual(
            "y must be an integer",
            str(err.exception))
        s1 = Square(2, 3, 4, "sdf")
        self.assertEqual(s1.id, "sdf")
        s2 = Square(2, 3, 4, False)
        self.assertEqual(s2.id, False)

    def test_02(self):
        """Test void arguments"""
        with self.assertRaises(TypeError) as err:
            s = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(err.exception))

    def test_03(self):
        """Test - negative int"""
        with self.assertRaises(ValueError) as err:
            s1 = Square(-1)
        self.assertEqual(
            "width must be > 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s2 = Square(1, -2)
        self.assertEqual(
            "x must be >= 0",
            str(err.exception))
        with self.assertRaises(ValueError) as err:
            s1 = Square(1, 2, -4)
        self.assertEqual(
            "y must be >= 0",
            str(err.exception))
        s1 = Square(2, 3, 4, -5)
        self.assertEqual(s1.id, -5)

    def test_04(self):
        """Test - zero values"""
        s1 = Square(2, 0, 0, 0)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 0)
        with self.assertRaises(ValueError) as err:
            s1 = Square(0, 0, 0, 2)
        self.assertEqual(
            "width must be > 0",
            str(err.exception))
        self.assertEqual(s1.x, 0)

    def test_05(self):
        """Test - Areas"""
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s1 = Square(3, 3)
        self.assertEqual(s1.area(), 9)
        s1 = Square(4, 3, 5)
        self.assertEqual(s1.area(), 16)
        s1 = Square(5, 3, 6, 7)
        self.assertEqual(s1.area(), 25)

    def test_06(self):
        """Test - str"""
        s1 = Square(2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1 = Square(3, 3)
        self.assertEqual(s1.__str__(), "[Square] (2) 3/0 - 3")
        s1 = Square(4, 3, 5)
        self.assertEqual(s1.__str__(), "[Square] (3) 3/5 - 4")
        s1 = Square(5, 3, 6, 7)
        self.assertEqual(s1.__str__(), "[Square] (7) 3/6 - 5")

    def test_07(self):
        """Test - Update"""
        s1 = Square(2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(3)
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 2")
        s1.update(3, 4)
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 4")
        s1.update(3, 4, 6)
        self.assertEqual(s1.__str__(), "[Square] (3) 6/0 - 4")
        s1.update(3, 4, 6, 7)
        self.assertEqual(s1.__str__(), "[Square] (3) 6/7 - 4")

    def test_08(self):
        """Test - Update with names"""
        s1 = Square(2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(id=3)
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 2")
        s1.update(size=4, id=3)
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 4")
        s1.update(id=3, x=6, size=4)
        self.assertEqual(s1.__str__(), "[Square] (3) 6/0 - 4")
        s1.update(y=7, id=3, x=6, size=4)
        self.assertEqual(s1.__str__(), "[Square] (3) 6/7 - 4")
        s1.update(height=3)
        self.assertEqual(s1.__str__(), "[Square] (3) 6/7 - 4")

    def test_09(self):
        """Test - unknowm attribute"""
        s1 = Square(2)
        s1.update(hi=3)
        self.assertEqual(hasattr(s1, 'hi'), False)

    def test_10(self):
        """Test mod atribute by assignment"""
        s1 = Square(12)
        self.assertEqual(s1.size, 12)
        s1.size = 25
        self.assertEqual(s1.size, 25)
        with self.assertRaises(TypeError) as err:
            s1.size = "asdasd"
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.size = [44, 56]
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.size = True
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.size = {"aasd": 5}
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.size = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(err.exception))
        with self.assertRaises(TypeError) as err:
            s1.size = (5,)
        self.assertEqual(
            "width must be an integer",
            str(err.exception))

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

    def test_14(self):
        """Test - save_to_file - load_from_file method"""
        s1 = Square(2, 6, 2)
        Square.save_to_file([s1])
        datafromfile = Square.load_from_file()
        res = '[{"x": 6, "y": 2, "size": 2, "id": 1}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))
        string = ""
        for data in datafromfile:
            string += str(data)
        self.assertEqual(string, "[Square] (1) 6/2 - 2")

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


class TestBasepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        base = "models/base.py"
        test_base = "tests/test_models/test_base.py"
        result = style.check_files([base, test_base])
        self.assertEqual(result.total_errors, 0)


class TestDocs(unittest.TestCase):
    """test docstrings for base and test_base files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)
