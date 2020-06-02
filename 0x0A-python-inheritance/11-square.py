#!/usr/bin/python3
"""
module for Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle Class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
