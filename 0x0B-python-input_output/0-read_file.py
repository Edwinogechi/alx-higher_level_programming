#!/usr/bin/python3
"""Defines a function of reading files"""


def read_file(filename=""):
    """Reads the txt file and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
