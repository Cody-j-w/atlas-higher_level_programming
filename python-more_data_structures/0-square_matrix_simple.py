#!/usr/bin/python3
def sqr(i):
    res = i * i
    return res


def square_matrix_simple(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(sqr, matrix[i])))
    return new_matrix
