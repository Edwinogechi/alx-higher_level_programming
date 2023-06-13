#!/usr/bin/python3
"""Defines a function that returns a json string representation"""
import json


def to_json_string(my_obj):
    """Return json representation of a string object"""
    return json.dumps(my_obj)
