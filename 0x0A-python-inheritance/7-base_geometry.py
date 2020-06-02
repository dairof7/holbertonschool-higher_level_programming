#!/usr/bin/python3
""" this module createa class BaseGeometry"""


class BaseGeometry():
    """empty BaseGeometry class"""
    pass

    def area(self):
        """method area
        return a Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
