#!/usr/bin/python3


"""Print alphabet in lowercase, not followed by a new line."""
for chars in range(97, 122 + 1):
    print("{}".format(chr(chars)),end="")
