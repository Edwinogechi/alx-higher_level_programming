#!/usr/bin/python3
"""Defines a class, Rectangle"""


class Rectangle:
    """Represent a rectangle by both height and width"""
    def __init__(self, width=0, height=0):
        """Initializes a class object(Rectanle)

        Attributes:
            width(int): New rectangle width (private)
            height(int): New rectangle height (private)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and Set rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and Set the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the printable String representation of class object"""
        if self.width is 0 or self.height is 0:
            return ("")
        else:
            return ((('#' * self.width) + "\n") * self.height)[:-1]
