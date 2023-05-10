#!/usr/bin/python3

for chars in range(97, 122 + 1):
    if chr(chars) != 'e' and chr(chars) != 'q':
        print("{}".format(chr(chars)), end="")
