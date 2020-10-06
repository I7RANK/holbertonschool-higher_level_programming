#!/usr/bin/python3
""" bad int """


class MyInt(int):
    """ class rebert int """
    def __eq__(self, other):
        """ invert """
        return False

    def __ne__(self, other):
        """ invert """
        return True
