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
        super().__init__(id, x, y, size, size)

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        print("[Square] ({0}) {1}/{2} - {3}".format(i, x, y, s))
