#!/usr/bin/python3
""" this module contains the save_to_json_file function """


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w') as fl:
        json_str = json.dumps(my_obj)
        fl.write(json_str)
