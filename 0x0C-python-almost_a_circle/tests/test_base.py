#!/usr/bin/python3

"""
Unittest for Base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test number 0 for base"""
        b0 = Base(8)
        b1 = Base(-7)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b0.id, 8)
        self.assertEqual(b1.id, -7)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)

    def test_01(self):
        b0 = Base("string")
        self.assertEqual(b0.id, "string")

    def test_02(self):
        b0 = Base(None)
        self.assertEqual(b0.id, 1)

    def test_03(self):
        b0 = Base(0.06)
        self.assertEqual(b0.id, 0.06)

    def test_04(self):
        b0 = Base(False)
        self.assertEqual(b0.id, False)

    def test_06(self):
        b0 = Base(-126)
        self.assertEqual(b0.id, -126)

    def test_07(self):
        b0 = Base(0.06)
        self.assertEqual(str(type(b0)), "<class 'models.base.Base'>")

    def test_08(self):
        b0 = Base(4)
        self.assertEqual(Base.to_json_string([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]), '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')


if __name__ == '__main__':
    unittest.main()