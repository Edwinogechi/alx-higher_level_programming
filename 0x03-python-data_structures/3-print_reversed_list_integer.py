#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list:
        # Invert through the list
        for invert in reversed(my_list):
            print("{:d}".format(invert))
