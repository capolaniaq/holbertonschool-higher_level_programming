#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list[0] is None
    except Exception:
        print("")
        return 0
    for i, j in enumerate(my_list):
        if i == x:
            print("")
            return i
        else:
            print("{}".format(j), end="")
    if (i <= x):
        print("")
        return i + 1
