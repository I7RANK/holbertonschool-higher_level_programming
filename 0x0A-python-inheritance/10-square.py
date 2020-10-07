#!/usr/bin/python3
""" this module contains the class BaseGeometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ creates one square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
