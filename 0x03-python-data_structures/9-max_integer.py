#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    j = my_list[0]
    for i in list(my_list):
        if i > j:
            j = i
    return j
