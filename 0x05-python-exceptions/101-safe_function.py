#!/usr/bin/python3

def safe_function(fct, *args):

    from sys import stderr

    """Executes a function correctly.

    Args:
        fct: Pointer to a function to execute.
        *args: Arguments to be passed to fct.

    Returns:
        Result of the function if executed successfully.
        None if an exception error occurs while executing the function.
    """

    try:
        # Execute the function with the provided arguments
        outcome = fct(*args)

        return (outcome)

    except Exception as message:
        # Print the Exception message to stderr
        print("Exception:", message, file=stderr)
        return (None)
