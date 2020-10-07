#!/usr/bin/python3
""" this module contains the read_file function """


def read_lines(filename="", nb_lines=0):
    num_lines = 0
    with open(filename) as text:
        for line in text:
            num_lines += 1
            print(line, end="")
            if nb_lines > 0:
                if num_lines >= nb_lines:
                    break
