#!/usr/bin/python3
"""Defines a function that seraches and updates a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Search and insert lines containing certain string to a file
    Args:
        filename (string): Name of the particular file
        search_string (str): The text being searched for within file
        new_string (string): Text to be updated
    """
    text = []
    with open(filename, "r", encoding) as s:
        for text in s:
            line_list.append(text)
            if search_string in text:
                line_list.append(new_string)

    with open(filename, "w", encoding) as i:
        w.write(text)
