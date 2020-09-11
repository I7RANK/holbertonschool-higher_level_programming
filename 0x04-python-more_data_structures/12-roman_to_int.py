#!/usr/bin/python3
def roman_to_int(roman_string):
    prev = 0
    sum_roman = 0
    conver_roman = {}

    if not roman_string:
        return 0

    conver_roman['I'] = 1
    conver_roman['V'] = 5
    conver_roman['X'] = 10
    conver_roman['L'] = 50
    conver_roman['C'] = 100
    conver_roman['D'] = 500
    conver_roman['M'] = 1000
    prev = conver_roman[roman_string[0]]

    for i in roman_string:
        if conver_roman[i] > prev:
            sum_roman += conver_roman[i] - (prev * 2)
        else:
            sum_roman += conver_roman[i]
        prev = conver_roman[i]

    return sum_roman
