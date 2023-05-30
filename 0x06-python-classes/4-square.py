#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a class square."""

    def __init__(self, size=0):
        """Initialize a new square with size attributes.

        Args:
            size (int): Size of square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the present size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Takes and returns the current area of the square."""
        return (self.__size * self.__size)
