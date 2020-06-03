#!/usr/bin/python3
"""Module for read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines Class
    Print: lines of a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        i = len(open(filename).readlines())
        if nb_lines <= 0:
            for i in range(i):
                print(f.readline(), end="")
            print("")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
