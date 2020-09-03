#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hiddlist = dir(hidden_4)
    hiddlist.sort()
    for i in hiddlist:
        if i.startswith("__") != True:
            print(i)
