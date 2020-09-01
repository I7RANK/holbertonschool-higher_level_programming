#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{:c}".format(ord(str[i])), end="")
    print()
