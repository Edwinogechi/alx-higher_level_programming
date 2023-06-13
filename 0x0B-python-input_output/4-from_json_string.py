#!/usr/bin/python3
"""Defines a function that returns a JSON object representation"""
import json


def from_json_string(my_str):
    """Return the object JSON string representation

    Args:
        my_str: The object JSON string
    """
    return json.loads(my_str)
