#!/usr/bin/python3

"""
Module containing the Base class model
"""
import json
from os.path import isfile


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

    @classmethod
    def load_from_file(cls):
        """
        class method to load a list of instances from a file
        """
        filename = "{}.json".format(cls.__name__)
        if not isfile(filename):
            return []
        with open(filename, 'r') as file:
            obj_list = cls.from_json_string(file.read())
        inst_list = []
        for obj in obj_list:
            inst_list.append(cls.create(**obj))
        return inst_list

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create()
        class method to create a new instance of either a Rectangle or a Square
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj
