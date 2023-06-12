#!/usr/bin/python3
"""A module that defines a function testing an object as instance of class."""


def is_kind_of_class(obj, a_class):
    """Test if an object is an instance of a class or of class inherited
    from given class.

    Arguments:
        obj(any): object to be tested 
        class(type): The class to match against the given object
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
