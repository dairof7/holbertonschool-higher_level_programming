#!/usr/bin/python3
""" this module create square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle Class"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
