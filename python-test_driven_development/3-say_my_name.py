#!/usr/bin/python3

"""
Module containing a function that prints a name based on provided parameters
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name accepts two strings and prints them in the form of a greeting

    Args:
        first_name: the string that is the first name in the greeting
        last_name: the string that is the surname in the greeting
        defaults to an empty string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
