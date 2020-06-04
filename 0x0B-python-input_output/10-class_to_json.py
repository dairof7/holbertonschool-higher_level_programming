#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """class_to_json
    Return: dict of a clase"""
    return obj.__dict__
