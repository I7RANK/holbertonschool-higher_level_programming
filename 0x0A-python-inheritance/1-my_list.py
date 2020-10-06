#!/usr/bin/python3
""" this module contains the class MyList """


class MyList(list):
    """ class that inherit from list """
    def print_sorted(self):
        """ print a list sorted """
        print(sorted(self))
