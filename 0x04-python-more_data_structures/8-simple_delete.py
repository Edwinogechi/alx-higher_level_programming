#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    # Check if the key exists in the dictionary
    if a_dictionary.get(key) is not None:

        # If the key exists, remove it from the copy
        del a_dictionary[key]

    # Return the modified dictionary
    return a_dictionary
