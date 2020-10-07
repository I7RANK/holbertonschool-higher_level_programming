#!/usr/bin/python3
""" this module contains the read_file function """


def write_file(filename="", text=""):
    num_lines = 0
    with open(filename, 'w') as fl:
        num_lines = fl.write(text)
    return num_lines
