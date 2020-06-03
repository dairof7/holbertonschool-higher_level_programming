#!/usr/bin/python3
"""Module for read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines Class
    Print: lines of a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            for i, line in enumerate(f):
                print(line, end="")
            print("")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
