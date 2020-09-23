#!/usr/bin/python3
""" class square """


class Square:
    """ a class """
    def __init__(self,  size=0, position=(0, 0)):
        """ constructor
        Argumemts:
        size{int} -- the size of square
        position{tuple} -- tuple of 2 positive integers """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int) or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self._Square__size = size
        self._position = position

    def area(self):
        """ return the area of square """
        return self._Square__size * self._Square__size

    def my_print(self):
        """ print a square with # character """
        size = self._Square__size
        posi = self._position
        if size == 0:
            print()
        else:
            for i in range(size):
                for k in range(posi[0]):
                    print(end=" ")
                for j in range(size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """ return the square size """
        return self._Square__size

    @size.setter
    def size(self, value):
        """ updates the square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        """ return the position """
        return self._position

    @position.setter
    def position(self, value):
        """ setter the position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
