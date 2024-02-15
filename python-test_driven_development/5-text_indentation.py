#!/usr/bin/python3

"""
Module containing function that adds newlines to string after ., :, or ?
"""


def text_indentation(text):
    """
    Text_indentation prints string with newlines after a ., :, or ? character

    Args:
        text: the string to be printed
    """
    space = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if space:
            if text[i + 1] != " ":
                space = False
            continue
        print(text[i], end="")
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print("\n")
            if i + 1 < len(text) - 1:
                if text[i + 1] == " ":
                    space = True
