#!/usr/bin/python3
"""Defines a function that writes an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Args:
        my_obj: The object to write
        filename: The file to write and save to
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
