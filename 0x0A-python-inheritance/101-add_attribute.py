#!/usr/bin/python3
"""
module for add_attribute.
"""


def add_attribute(ob, name, value):
    """add atribute of an object"""
    if hasattr(ob, name) or not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, name, value)
