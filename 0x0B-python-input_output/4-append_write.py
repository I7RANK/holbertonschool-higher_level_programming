#!/usr/bin/python3
""" this module contains the read_file function """


def append_write(filename="", text=""):
    num_lines = 0
    with open(filename, 'a') as fl:
        num_lines = fl.write(text)
    return num_lines
