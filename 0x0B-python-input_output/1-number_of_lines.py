#!/usr/bin/python3
""" this module contains the read_file function """


def number_of_lines(filename=""):
    num_lines = 0
    with open(filename) as text:
        for line in text:
            num_lines += 1
    return num_lines
