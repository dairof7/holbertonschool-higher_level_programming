#!/usr/bin/python3
"""Module for read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines Class
    Print: lines of a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        i = 0
        for x in f:
            i += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines > i:
            read_data = f.read()
            print(read_data)
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
