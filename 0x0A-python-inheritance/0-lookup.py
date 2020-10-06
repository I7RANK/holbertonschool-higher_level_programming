#!usr/bin/python3
""" contains the lookup function """


def lookup(obj):
    """ print all properties and methods of the obj
    Arguments:
        obj{obj} - is the obj to print """
    print(dir(obj))
