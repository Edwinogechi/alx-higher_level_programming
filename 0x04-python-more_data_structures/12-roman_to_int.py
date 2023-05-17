#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) != str or roman_string is None:
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    digits = [rom_num[i] for i in roman_string] + [0]
    interger = 0

    for x in range(len(digits) - 1):
        if digits[x] >= digits[x + 1]:
            interger += digits[x]
        else:
            interger -= digits[x]

    return interger
