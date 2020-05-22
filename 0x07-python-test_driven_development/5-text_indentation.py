#!/usr/bin/python3
"""
Module text_indentation
module to ident a text
print a text
"""


def text_indentation(text):
    """this functions print a text
    insert newline where find a ".", "?", ":"
    """
    if type(text) != str or text is None:
        raise TypeError("text must be a string")
    sw = 0
    for i in text:
        if i in [".", "?", ":"]:
            print(i, end="\n\n")
            sw = 1
        else:
            if sw == 0:
                print(i, end="")
            else:
                if i == ' ':
                    pass
                else:
                    print(i, end="")
                    sw = 0
