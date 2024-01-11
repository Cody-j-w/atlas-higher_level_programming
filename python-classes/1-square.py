#!/usr/bin/python3

"""
This module contains the definition of a Square class with a size attribute
"""

class Square:
    """
    A Square class with a private size attribute
    """
    def __init__(self, size):
        """
        the __init__ method for the Square class
        
        Args:
            size (int): the size of the Square
        """
        self.__size = size
