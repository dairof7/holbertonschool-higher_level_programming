#!/usr/bin/python3
"""Module for Student Class"""


class Student():
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """[summary]

        Args:
            first_name ([type]): [first name]
            last_name ([type]): [last name]
            age ([type]): [age]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """[summary]

        Returns:
            [dict]: [dict of a class]
        """
        dictionary = self.__dict__
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if type(key) is not str:
                return self.__dict__
            else:
                if key in dictionary:
                    new_dict[key] = dictionary[key]
        return new_dict

    def reload_from_json(self, json):
        """[summary]

        Args:
            json ([dict]): [dict to replace]
        """
        for key, data in json.items():
            self.__dict__[key] = data
