#!/usr/bin/python3
"find the peak in a list"


def find_peak(list_of_integers):
    "find peak in a list"
    if list_of_integers:
        max_int = max(list_of_integers)
    else:
        max_int = None
    return max_int
