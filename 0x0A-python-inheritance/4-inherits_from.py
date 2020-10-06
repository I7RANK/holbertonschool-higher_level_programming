#!/usr/bin/python3
""" this module contains the inherits_from function """


def inherits_from(obj, a_class):
    """ checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    Argumets:
    obj{obj} - the object
    a_class{class} - the class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
