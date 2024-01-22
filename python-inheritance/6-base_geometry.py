#!/usr/bin/python3

"""
Module containing the BaseGeometry class
"""


class BaseGeometry:
    """
    The BaseGeometry class with unimplemented area method
    """
    def area(self):
        raise Exception("area() is not implemented")
