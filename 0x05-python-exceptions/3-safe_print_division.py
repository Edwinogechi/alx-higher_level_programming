#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b  # Try performing the division
    except (TypeError, ZeroDivisionError):
        div = None  # Assign None if specified error occurs
    finally:
        print("Inside result: {}".format(div))  # Print the div value
    return (div)
