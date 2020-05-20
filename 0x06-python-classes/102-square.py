#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    """ Class Square with constuctor method"""
    def __init__(self, size=0):
        """Initializes the class Square
        Arg
            size: size to initializate __size
        """
        if not(type(size) == int or type(size) == float):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of a square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter function of size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        setter function of attribute size
        Args:
            value: value for __size
        """
        if not(type(size) == int or type(size) == float):
            raise TypeError("size must be a number")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def __eq__(self, other):
        return (self.__size ** 2 == other.__size ** 2)

    def __lt__(self, other):
        return (self.__size ** 2 < other.__size ** 2)

    def __le__(self, other):
        return (self.__size ** 2 <= other.__size ** 2)

    def __ne__(self, other):
        return (self.__size ** 2 != other.__size ** 2)

    def __gt__(self, other):
        return (self.__size ** 2 > other.__size ** 2)

    def __ge__(self, other):
        return (self.__size ** 2 >= other.__size ** 2)
