#!/usr/bin/python3
"""A module that defines a class BaseGeometry inherited ."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class defining a rectangle using B """

    def __init__(self, width, height):
        """Instantiates class object Rectangle

        Arguments:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Takes the area of the object (rectangle)"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the triangle"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
