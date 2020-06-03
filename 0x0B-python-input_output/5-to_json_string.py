#!/usr/bin/python3

"""Module for to_json_string"""


import json


def to_json_string(my_obj):
    """to_json_string Class
    returns the JSON representation of an object"""
    return json.dumps(my_obj)
