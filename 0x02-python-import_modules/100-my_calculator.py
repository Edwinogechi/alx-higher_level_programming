#!/usr/bin/python3

if __name__ == "__main__":

    # Import the functions from calculator_1.py
    from calculator_1 import add, sub, mul, div
    # Import the sys module for command line arguments
    import sys

    # Check that the correct number of arguments have been provided
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Create a dictionary of operators and functions
    opers = {"+": add, "-": sub, "*": mul, "/": div}

    # Check that the operator provided is valid
    if sys.argv[2] not in list(opers.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Convert the first and third command line arguments to integers
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the operation and print the result
    print("{} {} {} = {}".format(a, sys.argv[2], b, opers[sys.argv[2]](a, b)))
