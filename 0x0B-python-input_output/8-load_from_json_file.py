#!/usr/bin/python3
""" this module contains the load_from_json_file function """


import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename) as fl:
        for i in fl:
            return json.loads(i)
