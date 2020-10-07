#!/usr/bin/python3
""" this module contains the append_write function """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file and
    return the number of lines """
    num_lines = 0
    with open(filename, 'a') as fl:
        num_lines = fl.write(text)
    return num_lines
