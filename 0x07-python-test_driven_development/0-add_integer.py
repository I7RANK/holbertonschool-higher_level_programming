#!/usr/bin/python3
"""
thsi module contains the add_integer function


"""


def add_integer(a, b=98):
    """ this function adds 2 numbers
    a {int} -- number number one
    b {int} -- number number two :V """
    sum = 0
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    sum = a + b
    return sum
