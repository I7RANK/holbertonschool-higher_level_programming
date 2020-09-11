#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    names = []
    for i in a_dictionary:
        names.append(i)

    names.sort()

    for i in names:
        print("{}: {}".format(i, a_dictionary.get(i)))
