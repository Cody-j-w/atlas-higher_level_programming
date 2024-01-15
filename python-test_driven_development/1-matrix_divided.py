#!/usr/bin/python3

"""
A module that contains a function to divide a matrix by a specified divisor
"""

def matrix_divided(matrix, div):
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    length = len(matrix[0])
    new_list = []
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        sublist = []
        for j in matrix[i]:
            sublist.append(round(j / div, 2))
        new_list.append(sublist)
    return new_list