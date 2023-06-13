#!/usr/bin/python3
"""Defines a function that returns a JSON string representation"""
import json


def to_json_string(my_obj):
    """Return JSON representation of a string object"""
    return json.dumps(my_obj)
