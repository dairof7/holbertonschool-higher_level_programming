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
        self.assertTrue(len(Base.__doc__) > 0)

    def test_class(self):
        """check class docstrings"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method(self):
        """check method docstrings"""
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)
