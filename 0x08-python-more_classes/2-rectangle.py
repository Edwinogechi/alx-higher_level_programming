#!/usr/bin/python3
"""Module that defines a class, rectangle"""


class Rectangle:
    """Defines a rectangle by both width and height."""

    def __init__(self, width=0, height=0):
        """Instantiates a class object (new Rectangle).

        Attributes:
            width (int): Width of the new rectangle(private).
            height (int): Height of the new rectangle(private).
        """
        self.width = width

        self.height = height

    @property
    def width(self):
        """Get and set the width of the Rectangle."""
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
        """Get and set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """Returns area of the Rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))
