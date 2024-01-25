#!/usr/bin/python3

"""
Module containing the Base class model
"""

class Base:
    """
    Base class model

    Attributes:
        __nb_objects: a count of instantiated objects, used to determine ids
        id: the identifying number of the instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
