#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for j in (matrix):
        a.append([i**2 for i in j])
    return a
# return [[i**2 for i in j] for j in matrix]
