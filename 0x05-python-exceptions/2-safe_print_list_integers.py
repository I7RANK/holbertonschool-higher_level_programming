def safe_print_list_integers(my_list=[], x=0):
    real_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_len += 1
        except (TypeError, ValueError):
            pass

    print()
    return real_len
