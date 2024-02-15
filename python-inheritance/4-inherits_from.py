#!/usr/bin/python3

"""
Module containing function that tells whether or not an object is an
instance of a subclass of the specified class
"""


def inherits_from(obj, obj_class):
    """
    inherits_from tells if an object is an instance of a subclass of the
    specified object class
    Args:
        obj: the object
        obj_class: the class that we want to know whether or not obj belongs to
    Returns:
        bool: True if obj is an instance of a subclass of obj_class
        False otherwise
    """

    if type(obj) is obj_class:
        return False
    return isinstance(obj, obj_class)
