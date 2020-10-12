#!/usr/bin/python3
"""Contains the class rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle

    Args:
        Base (class): the class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int, optional): value of x. Defaults to 0.
            y (int, optional): value of y. Defaults to 0.
            id (int, optional): id of this instance. Defaults to None.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """ GETTERS AND SETTERS
    """
    @property
    def width(self):
        """get width

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter

        Args:
            width (int): the width of rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get height

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter

        Args:
            height (int): the height of rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x

        Returns:
            int: the x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter

        Args:
            x (int): the x of rectangle
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y

        Returns:
            int: the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter

        Args:
            y (int): the y of rectangle
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return the rectangle area

        Returns:
            int: the rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """displays the rectangle usin the simbol #
        """
        simbol = '#'

        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print(simbol, end="")
            print()

    def __str__(self):
        """returns one rectangle in format readable

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        t_id = "({}) ".format(self.id)
        t_xy = "{}/{} ".format(self.__x, self.__y)
        t_wh = "- {}/{}".format(self.__width, self.__height)
        return "[Rectangle] " + t_id + t_xy + t_wh

    def update(self, *args, **kwargs):
        """ updates the values of one rectangle
            *args assigns an argument to each attribute
                ♪  1st argument should be the <id> attribute
                ♪  2nd argument should be the <width> attribute
                ♪  3rd argument should be the <height> attribute
                ♪  4th argument should be the <x> attribute
                ♪  5th argument should be the <y> attribute
            **kwargs is skipped if *args exists and is not empty
        """
        len_arg = len(args)
        i = 0

        while i < len_arg:
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]
            i += 1

        if not len_arg == 0:
            return

        for k, v in kwargs.items():
            if k == "id":
                self.id = v
            if k == "width":
                self.width = v
            if k == "height":
                self.height = v
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

    def to_dictionary(self):
        """returns the representation of a dictionary of one Rectangle

        Returns:
            dict: dictionary of one rectangle
        """
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['height'] = self.height
        new_dict['width'] = self.width
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
