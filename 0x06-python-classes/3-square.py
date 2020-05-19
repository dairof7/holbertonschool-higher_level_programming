#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    """ Class Square with constuctor method"""
    def __init__(self, size=0):
        """Initializes the class Square
        Arg
            size: size to initializate __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__Square__size = size

    def area(self):
        """
        Calculate the area of a square
        Returns:
            The area of the square
        """
        return self.__Square__size ** 2
