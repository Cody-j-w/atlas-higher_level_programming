#!/usr/bin/python3

"""
Module containing the lookup function, which returns a list of all of the
methods of the object class passed as a parameter
"""

def lookup(obj):
    """
    look up function accepts an object (e.g list, int, string) as a paramater
    and returns a list of all of the methods that object has

    Args:
        obj: the object type to retrieve the methods of
    """
    return [method for method in dir(obj) if callable(getattr(obj, method))]