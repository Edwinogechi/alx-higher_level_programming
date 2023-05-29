#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function correctly.

    Args:
        fct: Pointer to a function to execute.
        *args: Arguments to be passed to fct.

    Returns:
        Result of the function if executed successfully.
        None if an exception error occurs while executing the function.
    """

    try:

        outcome = fct(*args)

        return (outcome)

    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
