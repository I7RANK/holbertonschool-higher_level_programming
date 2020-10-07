#!/usr/bin/python3
""" this module contains the Student class """


class Student():
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ init
        Arg:
            first_name - the student first name
            last_name - the student last name
            age - the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return the dict """
        if attrs is None:
            return self.__dict__
        new_dic = {}
        for i in attrs:
            if i in self.__dict__ and type(i) is str:
                new_dic[i] = self.__dict__[i]
        return new_dic

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        self.__dict__["first_name"] = json["first_name"]
        self.__dict__["last_name"] = json["last_name"]
        self.__dict__["age"] = json["age"]
