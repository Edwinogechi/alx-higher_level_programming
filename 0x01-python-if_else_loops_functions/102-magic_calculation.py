#!/usr/bin/python3
def magic_calculation(a, b, c):
    # Check if a is less than b
    if a < b:
        return (c)
    # Check if c is greater than b
    if c > b:
        return (a + b)

    # If neither of the above conditions are true, return a*b - c
    return (a*b - c)
