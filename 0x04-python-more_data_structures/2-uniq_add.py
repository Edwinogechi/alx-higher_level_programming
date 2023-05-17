#!/usr/bin/python3
def uniq_add(my_list=[]):

    # Create a set from the input list to remove duplicates
    unique_list = set(my_list)
    # Initialize a variable to hold the sum of unique elements
    number = 0

    # Iterate over the unique elements in the set
    for j in unique_list:
        # Add each unique element to the sum
        number += j

    # Return the sum of unique elements
    return (number)
