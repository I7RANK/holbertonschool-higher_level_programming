#!/usr/bin/python3
"""
    this script adds all arguments to a Python list,
    and then save them to a file:
"""


import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


argv = sys.argv
filename = "add_item.json"
obj = []

try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    with open(filename, 'w') as fl:
        pass

if obj:
    obj = obj + argv[1:]
    save_to_json_file(obj, filename)
else:
    save_to_json_file(argv[1:], filename)
