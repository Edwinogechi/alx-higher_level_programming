#!/usr/bin/python3
"""A Module defining a function testing an object and an inherited class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Arguments:
        obj: The object to test
        class: The class to match against the object to test
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
