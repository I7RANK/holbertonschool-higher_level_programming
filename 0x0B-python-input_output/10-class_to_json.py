#!/usr/bin/python3
""" this module contains the class_to_json function """


def class_to_json(obj):
    """ return the dict """
    return obj.__dict__
