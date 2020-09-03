#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)

    def print_args(argc, argv):
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))

    if argc == 1:
        print(argc - 1, "arguments.")
    elif argc == 2:
        print(argc - 1, "argument:")
        print_args(argc, sys.argv)
    else:
        print(argc - 1, "arguments:")
        print_args(argc, sys.argv)
