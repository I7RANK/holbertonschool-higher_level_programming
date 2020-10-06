#!/usr/bin/python3
""" this module contains the class BaseGeometry """


class BaseGeometry():
    """ Class BaseGeometry """
    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value
        Arguments:
            name{str} - is one name
            value{int} - is one value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
