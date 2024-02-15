#!/usr/bin/python3

"""
Module containing function that tells whether or not an object is an
instance of a specified class, or inherits from the specified class
"""


def is_kind_of_class(obj, obj_class):
    """
    is_king_of_class tells if an object is a specified class or inherits
    from the specified class

    Args:
        obj: the object
        obj_class: the class that we want to know whether or not obj belongs to
    Returns:
        bool: True if obj and obj_class match, False otherwise
    """

    return isinstance(obj, obj_class)
