#!/usr/bin/python3
""" this module contains the is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ checks if is the same instance of the class
    Argumets:
    obj{obj} - the object
    a_class{class} - the class """
    return isinstance(obj, a_class)
