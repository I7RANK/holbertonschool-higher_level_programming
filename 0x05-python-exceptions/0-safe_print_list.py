#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for real_len in range(x):
            print(my_list[real_len], end="")
    except IndexError:
        print()
        return real_len
    print()
    return real_len + 1
