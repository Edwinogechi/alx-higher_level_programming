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
