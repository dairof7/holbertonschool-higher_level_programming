#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            for j, element in enumerate(row):
                if (len(row) - 1 == j):
                    print("{:d}".format(element))
                else:
                    print("{:d}".format(element), end=" ")
    else:
        print("")

        # resumed form#
        # for row in matrix:
        # print(" ".join("{:d}".format(element) for element in row))
