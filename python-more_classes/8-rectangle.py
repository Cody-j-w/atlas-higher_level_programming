#!/usr/bin/python3

"""
A module defining a Rectangle class
"""


class Rectangle:
    """
    the definition of the Rectangle class

    Attributes:
        number_of_instances: the number of Rectangle instances
        print_symbol: the symbol used for rectangle visualization
    """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        The __init__ method for the Rectangle class

        Args:
            width: define the X axis of the rectangle
            height: define the Y axis of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        rect_str = ""
        if self.height == 0 or self.width == 0:
            return rect_str
        for y in range(self.height):
            for x in range(self.width):
                rect_str += str(self.print_symbol)
            if y != self.height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        repr_str = "Rectangle({0}, {1})".format(self.width, self.height)
        return repr_str

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
