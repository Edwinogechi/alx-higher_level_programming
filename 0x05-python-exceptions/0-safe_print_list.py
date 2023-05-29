#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0  # Variable keeping track no. of elements printed

    for i in range(x):

        try:

            # Print elements at index i incrementing the count
            print("{}".format(my_list[i]), end="")

            count += 1

        # if index e is out of range, break the loop (IndexError)
        except IndexError:
            break

    # Print a new line separating the output
    print("")

    # Return the count of elements printed
    return(count)
