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
            self.__size = size

    def area(self):
        """
        Calculate the area of a square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print("")

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
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
