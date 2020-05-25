#!/bin/python3
""" this module create the class Reactangle"""


class Rectangle:
    """ Class Rectangle with constuctor and other methods"""
    pass

    def __init__(self, width=0, height=0):
        """Initializes the class Rectangle
        Arg
            width: width of the rectangle
            height: height of the retangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        getter function of width
        Returns:
            width of the Rectangle
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        setter function of attribute width
        Args:
            value: value for __width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        getter function of height
        Returns:
            height of the Rectangle
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        setter function of attribute height
        Args:
            value: value for __height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
