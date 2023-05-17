#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list to store keys that need to be deleted
    keys_to_delete = []

    # Iterate over the items of the dictionary
    for key, val in a_dictionary.items():
        # Check if the value matches the given value
        if val == value:
            # If there's a match, add the key to the keys_to_delete list
            keys_to_delete.append(key)

    # Iterate over the keys_to_delete list
    for key in keys_to_delete:
        # Delete the key from the dictionary
        del a_dictionary[key]

    # Return the modified dictionary
    return a_dictionary
