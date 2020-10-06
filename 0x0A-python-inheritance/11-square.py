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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ returns the area """
        return self.__width * self.__height


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ creates one square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
