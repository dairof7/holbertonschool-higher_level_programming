#!/usr/bin/python3

"""[module for append_after]"""


def append_after(filename="", search_string="", new_string=""):
    """[inserts a line of text to a file]

    Args:
        filename (str, optional): [name of the file]. Defaults to "".
        search_string (str, optional): [string to search]. Defaults to "".
        new_string (str, optional): [string to add]. Defaults to "".
    """
    str = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            str = str + line
            if search_string in line:
                str = str + new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str)
