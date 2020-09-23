#!/usr/bin/python3
""" class square """


class Square:
    """ a class """
    def __init__(self,  size=0):
        """ constructor
        Argumemts:
        size{int} -- the size of square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
