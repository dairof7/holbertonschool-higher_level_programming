#!/usr/bin/python3

"""Module for append_write"""


def append_write(filename="", text=""):
    """append_write Class
    create and append data into a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        n = f.write(text)
    return n
