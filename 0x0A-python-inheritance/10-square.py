#!/usr/bin/python3
""" this module create square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle Class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area of square
        Returns:
            int -- area
        """
        return self.__size ** 2
