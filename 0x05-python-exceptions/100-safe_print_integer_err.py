#!/usr/bin/python3

import sys


def safe_print_integer_err(value):

    """Prints an integer with "{:d}".format() and handles potential errors.

    Args:
        value: The integer value to be printed.

    Returns:
        True if the value is an integer and successfully printed.
        False if a TypeError occurs and prints the error to stderr.
    """
    try:
        print("{:d}".format(value))  # Prints integer value
        return (True)

    except(ValueError, TypeError):
        # Print the exception error message to stderr
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (False)
