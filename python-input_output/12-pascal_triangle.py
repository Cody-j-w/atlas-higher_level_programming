#!/usr/bin/python3

"""
module containing function to create a Pascal's triangle
"""


def pascal_triangle(n):
    """
    function that creates a Pascal's triangle from n
    Args:
        n: Integer
    """
    triangle = []
    for i in range(n):
        layer = []
        for j in range(i+1):
            if j > 0 and j < i and i > 0:
                layer.append(triangle[i-1][j-1] + triangle[i-1][j])
            else:
                layer.append(1)
        triangle.append(layer)
    return triangle
