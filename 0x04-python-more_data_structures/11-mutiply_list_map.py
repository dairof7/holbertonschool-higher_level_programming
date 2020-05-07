#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new_list = [number] * len(my_list)
    return list(map(lambda x, y: x * y, my_list, new_list))
