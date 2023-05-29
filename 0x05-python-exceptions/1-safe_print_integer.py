#!/usr/bin/python3

def safe_print_integer(value):

    try:

        # Print the value as an integer and return true if successful
        print("{:d}".format(value))

        return(True)

    # Return False if a ValueError or TypeError occurs
    except (ValueError, TypeError):
        return(False)
