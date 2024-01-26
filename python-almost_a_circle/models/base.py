#!/usr/bin/python3

"""
Module containing the Base class model
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Base class method to return a list of JSON stringified dictionaries of
        instances
        """
        empty_list = "[]"
        if list_dictionaries is None:
            return empty_list
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method to save a list of instances to a file
        """
        filename = "{}.json".format(cls.__name__)
        objects = []
        if list_objs is not None:
            for obj in list_objs:
                objects.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
