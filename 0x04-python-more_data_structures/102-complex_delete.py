#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.keys())
    data = list(a_dictionary.values())
    while value in data:
        valor = data.index(value)
        llave = key[valor]
        a_dictionary.pop(llave)
        key = list(a_dictionary.keys())
        data = list(a_dictionary.values())
    return a_dictionary
