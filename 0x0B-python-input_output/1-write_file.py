#!/usr/bin/python3
"""This module defines a text writing function of a text file"""


def write_file(filename="", text=""):
    """Writes string to text file
    Args:
        filename(string): name of the file to be written
        text(str): The text string to write to the file
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)
