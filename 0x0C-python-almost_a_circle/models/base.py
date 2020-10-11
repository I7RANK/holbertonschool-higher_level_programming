#!/usr/bin/python3
""" This module contais the class base
"""


import json


class Base():
    """ Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor
        The goal of it is to manage id attribute in all your future classes
        and to avoid duplicating the same code (by extension, same bugs)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns a representation in json str

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: str in json format
        """
        idx = False
        json_str = "["
        if list_dictionaries is None:
            return "[]"
        for i in list_dictionaries:
            if idx is True:
                json_str += ", "
            if type(i) is dict:
                json_str += json.dumps(i)
            idx = True
        json_str += "]"
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"

        obj = []

        try:
            with open(filename) as fl:
                for i in fl:
                    obj = json.loads(i)
        except FileNotFoundError:
            with open(filename, 'w') as fl:
                pass

        if list_objs is None:
            with open(filename, 'w') as fl:
                fl.write("[]")

        for i in list_objs:
            obj.append(i.to_dictionary())
        json_str = cls.to_json_string(obj)

        with open(filename, 'w') as fl:
            fl.write(json_str)
