#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        _list = list((sorted(a_dictionary.values())))
    else:
        return "None"
    return _list[-1]

# return (max(a_dictionary.values()) if a_dictionary else None)
