#!/usr/bin/python3
"""
Module print_square
module to print a square
"""


def print_square(size):
    """this functions print a square
    Print a square with #
    size: is the size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
