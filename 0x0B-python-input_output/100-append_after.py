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
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
