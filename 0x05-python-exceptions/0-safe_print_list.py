#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print("")
            return i

    else:
        print("")
        if i == 0:
            return i
        else:
            return i + 1
