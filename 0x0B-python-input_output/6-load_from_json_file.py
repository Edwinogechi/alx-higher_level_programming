#!/usr/bin/python3
"""Defines a function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a file-"JSON"""
    with open(filename, "r", encoding="utf") as f:
        return json.load(f)
