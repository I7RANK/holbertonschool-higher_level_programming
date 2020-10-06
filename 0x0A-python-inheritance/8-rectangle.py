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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Instantiation
        Arguments:
            width{int} - is the width of the rectangle
            height{int} - is the height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
