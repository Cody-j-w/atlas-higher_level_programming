#!/usr/bin/python3

"""
module containing a function that reads the contents of a file
"""


def read_file(filename=""):
    """
    read_file opens a file, reads its contents, and prints those contents
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
