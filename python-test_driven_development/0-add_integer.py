#!/usr/bin/python3
"""
a basic addition module
"""


def add_integer(a, b=98):
    """
    a basic addition function

    Args:
        a: the first integer added
        b: the second integer added
    Return:
        the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
