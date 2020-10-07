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

    def to_json(self):
        """ return the dict """
        return self.__dict__
