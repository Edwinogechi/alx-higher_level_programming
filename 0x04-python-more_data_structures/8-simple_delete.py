#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    # Create a copy of the dictionary
    modified_dictionary = a_dictionary.copy()

    # Check if the key exists in the dictionary
    if key in modified_dictionary:

        # If the key exists, remove it from the copy
        del modified_dictionary[key]

    # Return the modified dictionary
    return modified_dictionary
