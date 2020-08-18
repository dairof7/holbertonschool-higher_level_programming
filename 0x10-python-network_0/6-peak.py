#!/usr/bin/python3
"find the peak in a list"


def find_peak(list_of_integers):
    "find peak in a list"
    if len(list_of_integers) != 0:
        max_int = max(list_of_integers)
    else:
        max_int = None
    return max_int
