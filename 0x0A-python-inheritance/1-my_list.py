#!/usr/bin/python3
"""Inherit list class to MyList using sorted print method"""


class MyList(list):
    """MyList class inherits from list and implements sorted print method"""
    def print_sorted(self):
        """Print a list but sorted in ascending order"""
        print(sorted(self))
