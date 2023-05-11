#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = len(sys.argv)
    if arguments == 1:
        print("{} arguments. ".format(arguments - 1))
    elif arguments == 2:
        print("{} argument: ".format(arguments - 1))
    else:
        print("{} arguments:".format(arguments - 1))
    for a in range(1, arguments):
        print("{}: {}".format(a, sys.argv[a]))
