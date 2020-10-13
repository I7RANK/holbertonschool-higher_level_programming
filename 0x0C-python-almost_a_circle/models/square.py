#!/usr/bin/python3
"""This module contais the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square

    Args:
        Rectangle (class): Class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size (int): the size of the Square
            x (int, optional): num of x. Defaults to 0.
            y (int, optional): num of y. Defaults to 0.
            id (int, optional): the id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns one square in format readable

        Returns:
            str: [square] (<id>) <x>/<y> - <size>
        """
        t_id = "({}) ".format(self.id)
        t_xy = "{}/{} ".format(self.x, self.y)
        t_wh = "- {}".format(self.size)
        return "[Square] " + t_id + t_xy + t_wh

    @property
    def size(self):
        """getter size of square

        Returns:
            [int]: the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ super
        how use update function of rectangle to set in square
            ♪  El primer argumento debe ser el <id> atributo
            ♪  El segundo argumento debe ser el <size> atributo
            ♪  El tercer argumento debe ser el <x> atributo
            ♪  El cuarto argumento debe ser el <y> atributo
        """
        super().update(*args, **kwargs)
        len_arg = len(args)
        i = 0
        while i < len_arg:
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]
            i += 1

        for k, v in kwargs.items():
            if k == "size":
                self.size = v

    def to_dictionary(self):
        """returns the representation of a dictionary of one Square

        Returns:
            dict: dictionary of one Square
        """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
