#!/usr/bin/python3
""" this module create
a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """constructor method method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area Class"""
        return self.__width * self.__height

    def __str__(self):
        """str Class"""
        return "[Rectangle] {}/{}".format(str(self.__width), str(self.__height))
