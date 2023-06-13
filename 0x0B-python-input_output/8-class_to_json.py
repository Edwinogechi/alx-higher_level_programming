#!/usr/bin/python3
"""Defines a function which returns dict description with simple data structure
"""


def class_to_json(obj):
    """Return the dictionary representation for JSON object serialization

    Arg:
        obj: The JSOZ object to serialize
    """
    return obj.__dict__
