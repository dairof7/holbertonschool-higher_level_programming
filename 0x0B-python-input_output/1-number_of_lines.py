#!/usr/bin/python3
"""Module for number_of_lines"""


def number_of_lines(filename=""):
    """number_of_lines Class
    Return: number if lines of a file"""
    i = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in enumerate(f):
            i += 1
    return i
