#!/usr/bin/python3

"""
Module containing function to build a dictionary out of the attributes
of a class, for the purposes of JSON serialization
"""


def class_to_json(obj):
    """
    class_to_json takes the attributes of a provided object - obj - and
    places them into a dictionary format for JSON serialization

    Args:
        obj: the class object being serialized
    """
    return vars(obj)
