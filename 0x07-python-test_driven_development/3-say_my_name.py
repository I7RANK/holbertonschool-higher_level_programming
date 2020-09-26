#!/usr/bin/python3
""" this module contain the say_my_name function """


def say_my_name(first_name, last_name=""):
    """ prints a name with the format: My name is <first_name> <last_name>
    Arguments:
        first_name{str} - the first name
        last_name{str} - the last name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
