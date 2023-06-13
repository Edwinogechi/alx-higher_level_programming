#!/usr/bin/python3
"""Defines appending function of a string to a file"""


def append_write(filename="", text=""):
    """Append text-string to end of a file and return characters written

    Args:
        filename (str): The file to append to
        text (str): The text-string to append to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
