#!/usr/bin/python3

"""
Module containing function that tells whether or not a paramater is an
instance of a specified class
"""


def is_same_class(obj, obj_class):
    """
    is_same_class tells whether an object is a specified class or not

    Args:
        obj: the object
        obj_class: the class that we want to know whether or not obj belongs to
    Returns:
        bool: True if obj and obj_class match, False otherwise
    """
    if type(obj) is bool and obj_class is int:
        return False
    elif obj_class is object:
        return False
    else:
        return isinstance(obj, obj_class)
