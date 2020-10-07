#!/usr/bin/python3
""" this module contains the number_of_lines function """


def number_of_lines(filename=""):
    """ returns the number of lines """
    num_lines = 0
    with open(filename) as text:
        for line in text:
            num_lines += 1
    return num_lines
