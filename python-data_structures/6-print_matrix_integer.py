#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            temp = i[j]
            print("{:d}".format(temp), end=" " if j != len(i) - 1 else "\n")
