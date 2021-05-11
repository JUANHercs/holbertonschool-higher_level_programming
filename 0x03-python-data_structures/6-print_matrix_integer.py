#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for j in matrix:
        print(" ".join("{:d}".format(i) for i in j))
