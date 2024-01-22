#!/usr/bin/python3

"""
module containing the Square class, which inherits from the Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class is a subclass of Rectangle with similar methods
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {0}/{1}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
