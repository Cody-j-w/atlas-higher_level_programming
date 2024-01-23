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

    attrs = [att for att in dir(obj) if not callable(getattr(obj, att))]
    attr_dict = dict()
    for att in attrs:
        attr_dict[att] = obj.att
    return attr_dict
