#!/usr/bin/python3
"""Defines a function testing an object as a class instance"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of class

    Args:
        obj(any): The object to test
        class(type): The class to match the given object
    """
    if type(obj) == a_class:
        return True
    else:
        return False
