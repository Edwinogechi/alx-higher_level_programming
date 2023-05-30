#!/usr/bin/python3
"""Define a class Square by attributes"""


class Square:
    """Represent a class square"""
    def __init__(self, size=0):
        """Initialize class square with size attribute

        Args:
            size(int): The size of new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Print the square with # characters"""
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print("")

    def area(self):

        """Takes and returns the area of a square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Gets/sets the value of size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value of size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
