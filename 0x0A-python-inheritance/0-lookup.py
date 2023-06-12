#!/usr/bin/python3
"""This module defines and returns a list of all avialable attributes
and methods in a class object
"""


def lookup(obj):
    """Return available list class methods/attributes"""
    return dir(obj)
