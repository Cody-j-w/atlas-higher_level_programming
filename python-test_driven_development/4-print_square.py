#!/usr/bin/python3

"""
A module containing the print_square function
"""


def print_square(size):
    """
    print_square prints a square of "#" characters based on the provided size

    Args:
        An integer representing the dimensions of the square. Can't be negative
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
