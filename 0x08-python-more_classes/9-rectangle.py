#!/usr/bin/python3
"""Defines a class, Rectangle"""


class Rectangle:
    """Represent a rectangle by both height and width"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a class object(Rectanle)

        Attributes:
            width(int): New rectangle width (private)
            height(int): New rectangle height (private)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get and Set rectangle width"""
        return (self.__width)

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
        return (self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return the printable String representation of class object"""
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return (((str(self.print_symbol) * self.width) + '\n'
                     ) * self.height)[:-1]

    def __repr__(self):
        """Return the string representation of instance(Rectangle)"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Delete a Rectangle and print a message on each deletion."""
        type(self).number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles by area and returns one with greater area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with both the width and height equal in size.

        Attributes:
            size (int): Width and Height of the new class instance (Rectangle).
        """
        return (cls(size, size))
