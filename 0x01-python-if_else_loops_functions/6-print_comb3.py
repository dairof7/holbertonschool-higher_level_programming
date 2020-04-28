#!/usr/bin/python3
for i in range(0, 100):
    d1 = int(i / 10)
    d2 = i % 10
    if d1 < d2:
        if i == 89:
            print("{:d}".format(i))
        else:
            print("{:02d}, ".format(i), end="")
