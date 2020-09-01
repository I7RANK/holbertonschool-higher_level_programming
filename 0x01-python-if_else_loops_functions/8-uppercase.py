#!/usr/bin/python3
def uppercase(str):
    rest = 0

    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            rest = 32
        print("{:c}".format(ord(str[i]) - rest), end="")
        rest = 0
    print()
