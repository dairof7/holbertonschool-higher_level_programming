#!/usr/bin/python3
"""Unittest for rectangle file: class and methods"""

import pep8
import unittest
import sys
from models import rectangle
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO


class Test_Rectangle_outputs(unittest.TestCase):
    """Test_Rectangle_outputs test for Rectangle subclass"""

    def test_id_setting(self):
        """test_id_setting method that test the id input"""
        Base._Base__nb_objects = 0
        Rec1 = Rectangle(2, 3)
        self.assertEqual(Rec1.id, 1)
        Rec2 = Rectangle(4, 3)
        self.assertEqual(Rec2.id, 2)
        Rec3 = Rectangle(4, 5, 3, 3, 4)
        self.assertEqual(Rec3.id, 4)
        Rec4 = Rectangle(2, 6)
        self.assertEqual(Rec4.id, 3)
        Rec5 = Rectangle(3, 7, 3, 2, -4)
        self.assertEqual(Rec5.id, -4)

    def test_area_method(self):
        """test_area_method method to test output
        of area method for rectangle instances"""
        Base._Base__nb_objects = 0
        Rec6 = Rectangle(2, 3)
        self.assertEqual(Rec6.area(), 6)
        Rec7 = Rectangle(6, 5)
        self.assertEqual(Rec7.area(), 30)

    def test_display_method(self):
        """test_display_method method to test output
        of area method for rectangle instances"""
        Base._Base__nb_objects = 0
        Rec8 = Rectangle(3, 3)
        printed_stream = StringIO()
        sys.stdout = printed_stream
        Rec8.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_stream.getvalue(), "###\n###\n###\n")
        Rec9 = Rectangle(3, 3, 1, 1)
        printed_stream2 = StringIO()
        sys.stdout = printed_stream2
        Rec9.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_stream2.getvalue(), "\n ###\n ###\n ###\n")

    def test_str_method(self):
        """test_str_method to test str output"""
        Base._Base__nb_objects = 0
        Rec12 = Rectangle(2, 6)
        self.assertEqual(Rec12.__str__(), "[Rectangle] (1) 0/0 - 2/6")
        Rec13 = Rectangle(2, 3, 3, 3, 12)
        self.assertEqual(Rec13.__str__(), "[Rectangle] (12) 3/3 - 2/3")

    def test_update_method(self):
        """test_update_method to test update instance method"""
        Base._Base__nb_objects = 0
        Rec_up = Rectangle(3, 2, 4, 5)
        # testing *args
        Rec_up.update(3)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (3) 4/5 - 3/2")
        Rec_up.update(3, 4)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (3) 4/5 - 4/2")
        Rec_up.update(3, 4, 5)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (3) 4/5 - 4/5")
        Rec_up.update(3, 4, 5, 6)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (3) 6/5 - 4/5")
        Rec_up.update(3, 4, 5, 6, 7)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (3) 6/7 - 4/5")
        # testing **kwargs
        Rec_up.update(id=12)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (12) 6/7 - 4/5")
        Rec_up.update(id=12, width=3)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (12) 6/7 - 3/5")
        Rec_up.update(id=12, width=3, height=8)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (12) 6/7 - 3/8")
        Rec_up.update(id=12, width=3, height=8, x=2)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (12) 2/7 - 3/8")
        Rec_up.update(id=12, width=3, height=8, x=2, y=9)
        self.assertEqual(Rec_up.__str__(), "[Rectangle] (12) 2/9 - 3/8")

    def test_to_dictionary(self):
        """test_to_dictionary test method output"""
        Base._Base__nb_objects = 0
        R = Rectangle(2, 3, 2, 2, 1)
        out_expect = {'x': 2, 'y': 2, 'width': 2, 'height': 3, 'id': 1}
        self.assertEqual(R.to_dictionary(), out_expect)


class TestRaiseExceptions(unittest.TestCase):
    """TestRaiseExceptions test exceptions for rectangle subclass"""

    def test_not_int_input(self):
        """test_not_int_input method to test not int input
        for width, height, x, and y attributes"""
        Base._Base__nb_objects = 0
        # width argument not int
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rec14 = Rectangle("width", 2, 3, 4)
        # height argument not int
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rec15 = Rectangle(3, "Height", 3, 4)
        # x argument not int
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rec16 = Rectangle(6, 2, "x", 4)
        # y argument not int
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rec17 = Rectangle(8, 2, 3, "y")

    def test_input_under_or_equal_0(self):
        """test_input_under_or_equal_0 method that test setter
        validation of width, height, x and y attributes"""
        Base._Base__nb_objects = 0
        # width argument < 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rec18 = Rectangle(-2, 2, 3, 4)
        # width argument == 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rec19 = Rectangle(0, 7, 3, 4)
        # height argument < 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rec20 = Rectangle(6, -3, 3, 4)
        # height argument == 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rec21 = Rectangle(8, 0, 3, 4)
        # x argument < 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rec22 = Rectangle(6, 3, -3, 4)
        # y argument < 0
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rec23 = Rectangle(6, 3, 3, -1)


class TestRectanglepep8(unittest.TestCase):
    """Validate pep8"""

    def test_pep8(self):
        """test for base file and test_base file pep8"""
        style = pep8.StyleGuide(quiet=True)
        rectangle = "models/rectangle.py"
        test_rectangle = "tests/test_models/test_rectangle.py"
        result = style.check_files([rectangle, test_rectangle])
        self.assertEqual(result.total_errors, 0)


class TestDocs(unittest.TestCase):
    """test docstrings for rectangle and test_rectangle files"""

    def test_module(self):
        """check module docstrings"""
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
