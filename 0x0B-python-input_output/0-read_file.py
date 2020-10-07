#!/usr/bin/python3
""" this module contains the read_file function """


def read_file(filename=""):
    with open(filename) as text:
        for line in text:
            print(line, end="")
