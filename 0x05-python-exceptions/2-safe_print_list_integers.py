#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_count = 0  # Variable to track the no. of elements prnted

    for e in range(x):
        try:
            if isinstance(my_list[e], int):  # Check for intergers

                """Print the interger followed by a new line"""
                print("{:d}".format(my_list[e]), end=" ")
                int_count += 1  # Increse the count of integers printed by one
        except(IndexError):
            break

    print("")  # Print a new line separating the outcome

    return(int_count)  # Return count of integers printed
