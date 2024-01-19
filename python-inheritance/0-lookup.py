#!/usr/bin/python3

"""
Module containing the lookup function, which returns a list of all of the
methods of the object class passed as a parameter

Args:
    obj: an object
"""

def lookup(obj):
    return dir(obj)
