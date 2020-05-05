#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return ("None")
    else:
        mayor = my_list[0]
        for i in my_list[1:]:
            if i > mayor:
                mayor = i
        return mayor
