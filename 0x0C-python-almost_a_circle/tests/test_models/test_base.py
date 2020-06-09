#!/usr/bin/python3
"""Unittest for base file: class and methods"""

import pep8
import unittest
import os
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base_outputs(unittest.TestCase):
    """Test_Base_outputs test for Base class"""

    def test_id_setting(self):
        """test_id_setting method that test the setting of id
        and it's output"""
        Base._Base__nb_objects = 0

        base_1 = Base()
        self.assertEqual(base_1.id, 1)

        base_2 = Base()
        self.assertEqual(base_2.id, 2)

        base_3 = Base(4)
        self.assertEqual(base_3.id, 4)

        base_4 = Base()
        self.assertEqual(base_4.id, 3)

        base_5 = Base(-4)
        self.assertEqual(base_5.id, -4)

        base_6 = Base(None)
        self.assertEqual(base_6.id, 4)
        base_6 = Base(None)
        self.assertEqual(base_6.id, 5)

    def test_to_json_string(self):
        """test_to_json_string test the output of the staticmethod
        of Base class"""
        Base._Base__nb_objects = 0

        python_dict = {'id': 1, 'x': 3, 'y': 2, 'width': 1, 'height': 2}
        json_string = Base.to_json_string([python_dict])
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(python_dict), dict)

        # test empty dict
        python_dict = {}
        json_string = Base.to_json_string(python_dict)
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(python_dict), dict)

    def test_save_to_file(self):
        """test_save_to_file test the output of the classmethod"""
        Base._Base__nb_objects = 0

        # test if the file was created
        Rec1 = Rectangle(2, 3)
        Rec2 = Rectangle(3, 4)
        Rectangle.save_to_file([Rec1, Rec2])
        self.assertEqual(os.path.exists("Rectangle.json"), True)

        Sq1 = Square(3)
        Sq2 = Square(4)
        Square.save_to_file([Rec1, Rec2])
        self.assertEqual(os.path.exists("Square.json"), True)

    def test_from_json_string(self):
        """test_from_json_string test the output of staticmethod"""
        Base._Base__nb_objects = 0

        python_dict_list = []
        dict1 = {'id': 1, 'x': 4, 'y': 2, 'width': 1, 'height': 2}
        dict2 = {'id': 2, 'x': 3, 'y': 2, 'width': 1, 'height': 2}
        python_dict_list.append(dict1)
        python_dict_list.append(dict2)
        json_string = Rectangle.to_json_string(python_dict_list)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_output, python_dict_list)

        python_dict_list = []
        json_string = Rectangle.to_json_string(python_dict_list)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_output, python_dict_list)
        # Consider input not as a json string

    def test_create(self):
        """test_create test output of classmethod"""
        Base._Base__nb_objects = 0

        Rec1 = Rectangle(3, 2)
        Rec2_copy = Rectangle.create(**Rec1.to_dictionary())
        self.assertEqual(Rec1.to_dictionary(), Rec2_copy.to_dictionary())
        self.assertEqual(Base._Base__nb_objects, 2)

        Sq1 = Square(4)
        Sq2_copy = Square.create(**Sq1.to_dictionary())
        self.assertEqual(Sq1.to_dictionary(), Sq2_copy.to_dictionary())
        self.assertEqual(Base._Base__nb_objects, 4)

        # testing from not create instance
        Base._Base__nb_objects = 0

        dict_R1 = {'width': 3, 'height': 7, 'x': 3, 'y': 4, 'id': 2}
        Rec1 = Rectangle.create(**dict_R1)
        self.assertEqual(Rec1.to_dictionary(), dict_R1)
        self.assertEqual(Base._Base__nb_objects, 1)

        dict_S1 = {'size': 6, 'x': 1, 'y': 3, 'id': 5}
        Rec1 = Rectangle.create(**dict_R1)
        self.assertEqual(Rec1.to_dictionary(), dict_R1)
        self.assertEqual(Base._Base__nb_objects, 2)

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


if __name__ == "__main__":
    unittest.main()
