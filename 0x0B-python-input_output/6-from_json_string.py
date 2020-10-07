#!/usr/bin/python3
""" this module contains the from_json_string function """


import json


def from_json_string(my_str):
    """ returns an object (Python) represented by a JSON string: """
    return json.loads(my_str)
