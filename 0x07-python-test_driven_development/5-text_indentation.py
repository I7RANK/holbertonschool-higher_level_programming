#!/usr/bin/python3
""" this module contain the  text_identation function"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters:
    '.'  '?'  ':'
    Arguments:
    text{str} - is the text"""

    lchar = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in lchar:
            print("{}\n".format(text[i]))
            i += 1

            try:
                while text[i] == ' ':
                    i += 1
            except IndexError:
                break
        print(text[i], end="")
        i += 1
