#!/usr/bin/python3
""" module for inherit_form"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class
    that inherited (directly or indirectly) """
    return isinstance(obj, a_class) and not type(obj) == a_class
