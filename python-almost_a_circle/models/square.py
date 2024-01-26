#!/usr/bin/python3

"""
module containing Square subclass model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square subclass of Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return "[Square] ({0}) {1}/{2} - {3}".format(i, x, y, s)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update method for Square class
        Accepts a list of arguments and updates attributes in a set order
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        return a dictionary of the calling instance's attributes
        """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return {'id': i, 'size': s, 'x': x, 'y': y}