#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """write_file Class
    create and write data into a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        n = f.write(text)
    return n
