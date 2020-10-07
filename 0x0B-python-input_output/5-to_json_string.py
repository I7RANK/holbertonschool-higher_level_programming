#!/usr/bin/python3
""" this module contains the read_file function """


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string): """
    str_json = json.dumps(my_obj)
    return str_json
