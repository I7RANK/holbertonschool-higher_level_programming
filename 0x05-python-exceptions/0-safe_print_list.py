#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_len = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            real_len += 1
    except IndexError:
        print()
        return i
    print()
    return i + 1
