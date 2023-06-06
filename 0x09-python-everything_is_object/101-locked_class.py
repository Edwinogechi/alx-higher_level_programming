#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    User prevented from initializing new lockedclass attributes
    unless the attribute is called 'first_name'
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=None):
        self.first_name = first_name
