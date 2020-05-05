#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print("")
        # resumed form#
        # print(" ".join("{:d}".format(element) for element in row))
