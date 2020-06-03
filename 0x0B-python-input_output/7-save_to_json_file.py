#!/usr/bin/python3
"""Module for to_json_string"""


import json


def save_to_json_file(my_obj, filename):
    """from_json_string Class
    writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_file = json.dumps(my_obj)
        file_a.write(json_file)
