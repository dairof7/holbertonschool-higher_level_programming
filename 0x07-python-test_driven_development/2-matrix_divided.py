#!/usr/bin/python3
"""
Module matrix_divided
module to div elements of a matrix
Return: new matrix divided by div
"""


def matrix_divided(matrix, div):
    """this functions divided a matrix
    Return matrix divided by div
    """
    res = []
    files = []
    a = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(a)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) != list:
            raise TypeError(a)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(a)
            files.append(round(j / div, 2))
        res.append(files)
        files = []
    return res
