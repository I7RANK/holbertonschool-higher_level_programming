#!/usr/bin/python3
"""This module contais the class base
"""


import json


class Base():
    """Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
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
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writhes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"

        obj = []

        """ try:
            with open(filename) as fl:
                for i in fl:
                    obj = json.loads(i)
        except FileNotFoundError:
            with open(filename, 'w') as fl:
                pass """

        if list_objs is None:
            with open(filename, 'w') as fl:
                fl.write("[]")
            return

        for i in list_objs:
            obj.append(i.to_dictionary())
        json_str = cls.to_json_string(obj)

        with open(filename, 'w') as fl:
            fl.write(json_str)

    def from_json_string(json_string):
        """returns a list of the JSON string representation

        Args:
            json_string (str): json string

        Returns:
            list: if json_string is None return an empy list
            or the list represented by json string
        """
        if json_string is None:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
            with the attributes that there are in **dictionary

        Returns:
            Instance: a instacne of Rectangle or Square
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """reads a JSON file and creates a list of instances
            with the contend of the file

        Returns:
            list: list of instances
        """
        filename = cls.__name__ + ".json"
        json_string = ""
        list_instances = []

        try:
            with open(filename) as fl:
                json_string = fl.read()
        except FileNotFoundError:
            return list()

        list_from_json = cls.from_json_string(json_string)

        for i in list_from_json:
            list_instances.append(cls.create(**i))

        return list_instances
