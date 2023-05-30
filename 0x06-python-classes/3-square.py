#!/usr/bin/python3
"""Define a class Square with attributes"""


class Square:
    """Represents a class square"""
    def __init__(self, size=0):
        """Instantiates class object of the square with size attribute

        Args:
            size: size of the new square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Takes and returns the current area of a square
        """
        return (self.__size * self.__size)
