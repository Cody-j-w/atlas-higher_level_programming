#!/usr/bin/python3

"""
This module contains the definition of a Square class with a size attribute
"""


class Square:
    """
    A Square class with a private size attribute
    """
    def __init__(self, size=0):
        """
        the __init__ method for the Square class

        Args:
            size (int): the size of the Square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size private attribute

        Args:
            value: the value to set size as
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A method of Square that returns the square area

        Return:
            the square area of the calling instance of Square
        """
        return self.size * self.size

    def my_print(self):
        """
        print the area of the square
        """
        if self.size < 1:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
