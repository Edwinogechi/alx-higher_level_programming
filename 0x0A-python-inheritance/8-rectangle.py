#!/usr/bin/python3
"""A module that defines an empty class BaseGeometry."""


class BaseGeometry:
    """An empty class that represent base geometry."""

    def area(self):
        """The area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name associated with the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
