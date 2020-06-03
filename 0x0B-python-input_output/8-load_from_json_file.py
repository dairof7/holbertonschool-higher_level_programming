#!/usr/bin/python3
"""Module for load_from_json_file"""


import json


def load_from_json_file(filename):
    """from_json_string Class
    creates an Object from a “JSON file
    Return: # of characteres""""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
