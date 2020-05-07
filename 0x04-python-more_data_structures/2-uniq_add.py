#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    for j, i in enumerate(my_list):
        if i not in my_list[0:j]:
            _sum += i
    return _sum
# _sum = sum(set(my_list))
