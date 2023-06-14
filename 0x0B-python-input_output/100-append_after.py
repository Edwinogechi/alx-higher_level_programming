#!/usr/bin/python3
"""Defines a function that searches and updates a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Search and insert lines containing certain string to a file
    Args:
        filename (str): Name of the particular file
        search_string (str): The text being searched for within file
        new_string (str): Text to be updated
    """
    lines = []
    with open(filename, "r") as r:
        for line in r:
            lines += line
            if search_string in line:
                lines += new_string

    with open(filename, "w") as w:
        w.write(lines)
