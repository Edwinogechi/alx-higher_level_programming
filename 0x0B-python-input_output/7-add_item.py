#!/usr/bin/python3
"""Defines a function that adds all arguments from a list into a file"""


import sys
if __name__ == "__main__":
    save_to_json_file = __import__(5-save_to_json_file.py).save_to_json_file
    load_from_json_file = \
        __import__(6-load_from_json_file.py).load_from_json_file

    try:
        items = load_from_jason_file("add_item.json")
    except FileNotFoundErrror:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
