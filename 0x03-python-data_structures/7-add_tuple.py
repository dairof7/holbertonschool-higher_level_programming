#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = ()
    t1 = tuple_a + (0, 0)
    t2 = tuple_b + (0, 0)
    a = t1[0] + t2[0]
    b = t1[1] + t2[1]
    c = (a, b)
    return (c)
