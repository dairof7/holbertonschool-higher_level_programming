#!/usr/bin/python3

"""Module for read_file"""


def read_file(filename=""):
    """read_file Class
    print data from a file"""
    with open(filename, 'r') as f:
        data = f.read()
    print(data, end="")
