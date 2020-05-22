#!/usr/bin/python3
"""
Module say_my_name
module to print the name
"""


def say_my_name(first_name, last_name=""):
    """this functions print the name
    print the name : My name is <first name> <last name>
    first_name: the first name
    last_name: the last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
