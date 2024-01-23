#!/usr/bin/python3

"""
module containing function to append content to a file
"""


def append_write(filename="", content=""):
    """
    Append content to a specified file

    Args:
        filename: the name of the file. Created if it doesn't exist
        content: the content to add to filename
    """

    with open(filename, 'a') as file:
        file.write(content)
    return len(content)
