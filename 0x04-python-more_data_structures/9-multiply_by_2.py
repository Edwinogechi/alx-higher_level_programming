#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    # Create a new dictionary to store the multiplied values
    new_dictionary = {}

    # Iterate over the key-value pairs of the input dictionary
    for key, value in a_dictionary.items():

        # Multiply each value by 2 and store it in the new dictionary
        new_dictionary[key] = value * 2

    # Return the new dictionary with multiplied values
    return new_dictionary
