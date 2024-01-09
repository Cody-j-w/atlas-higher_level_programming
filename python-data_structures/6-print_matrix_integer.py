#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            for j in range(len(i)):
                t = i[j]
                print("{}".format(t), end=" " if j != len(i) - 1 else "\n")
