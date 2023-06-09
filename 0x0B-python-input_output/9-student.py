#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Initializes a new instance - Student

    Attributes:
        first_name (str): The first name of student
        last_name (str): The last name of student
        age (int): The age of the student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiate class object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Find dict representation of instance(student)"""
        return self.__dict__
