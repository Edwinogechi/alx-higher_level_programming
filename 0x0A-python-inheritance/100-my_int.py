#!/usr/bin/python3
"""This module defines a class MyInt that inherits int"""


class MyInt(int):
    """Invert equality operators on int"""
    def __eq__(self, value):
        """Override equal if not equal"""
        if self != value:
            return True
        else:
            return False

    def __ne__(self, value):
        """Override not equal if equal"""
        if self == value:
            return True
        else:
            return False
