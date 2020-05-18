#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    r = None
    try:
        r = fct(*args)
        return r
    except Exception as err:
        print("Exception:", err, file=stderr)
