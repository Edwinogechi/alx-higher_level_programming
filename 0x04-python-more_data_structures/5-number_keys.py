#!/usr/bin/python3
def number_keys(a_dictionary):

    # Initialize a variable to hold the count of keys in the dictionary
    number = 0
    # Convert the keys of the dictionary into a list
    list_keys = list(a_dictionary.keys())

    # Iterate over the keys in the list
    for i in list_keys:

        # Increment the count for each key
        number += 1

    # Return the count of keys in the dictionary
    return (number)
