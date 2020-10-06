#!/usr/bin/python3
""" this module contains the is_same_class function """


def is_same_class(obj, a_class):
    """ checks if is the same instance of the class
    Argumets:
    obj{obj} - the object
    a_class{class} - the class """
    return type(obj) == a_class
