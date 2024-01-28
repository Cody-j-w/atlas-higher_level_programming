#!/usr/bin/python3

"""
Module containing Rectangle class model, inheriting from Base class model
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(i, x, y, w, h)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the total area of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        display a visual representation of the Rectangle instance
        """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """
        update method for Rectangle class
        Accepts a list of arguments and updates attributes in a set order
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        return a dictionary of the calling instance's attributes
        """
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return {'id': i, 'width': w, 'height': h, 'x': x, 'y': y}
