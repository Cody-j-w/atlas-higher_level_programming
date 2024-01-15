#!/usr/bin/python3

"""
A module that contains a function to divide a matrix by a specified divisor
"""


def matrix_divided(matrix, div):
    """
    A function that accepts a matrix (and only a matrix) and divides
    the elements of each list therein

    Args:
        matrix: the matrix to be iterated and divided
        div: the divisor that all elements will be divided by
    """

    """
    Errors
    """
    DivError = "div must be a number"
    MatrixError = "matrix must be a matrix (list of lists) of integers/floats"
    ZeroError = "division by zero"
    SizeError = "Each row of the matrix must have the same size"

    if type(div) is not int and type(div) is not float:
        raise TypeError(DivError)
    if type(matrix) is not list:
        raise TypeError(
            MatrixError
            )
    if div == 0:
        raise ZeroDivisionError(ZeroError)
    if type(matrix[0]) is not list:
        raise TypeError(MatrixError)
    length = len(matrix[0])
    new_list = []
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(MatrixError)
        if len(matrix[i]) != length:
            raise TypeError(SizeError)
        sublist = []
        for j in matrix[i]:
            if type(j) is not int and type(j) is not float:
                raise TypeError(MatrixError)
            sublist.append(round(j / div, 2))
        new_list.append(sublist)
    return new_list
