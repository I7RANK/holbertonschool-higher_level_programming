#!/usr/bin/python3
""" this module contains the class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
