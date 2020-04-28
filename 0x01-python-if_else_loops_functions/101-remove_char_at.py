#!/usr/bin/python3
def remove_char_at(str, n):
    r = ""
    for j, i in enumerate(str):
        if (j != n):
            r = r + i
    return r
