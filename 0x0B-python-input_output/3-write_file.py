#!/usr/bin/python3
""" this module contains the write_file function """


def write_file(filename="", text=""):
    """ writes a text in a file and return the number of lines written """
    num_lines = 0
    with open(filename, 'w') as fl:
        num_lines = fl.write(text)
    return num_lines
