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

    def to_json(self):
        """[summary]

        Returns:
            [dict]: [dict of a class]
        """
        return self.__dict__
