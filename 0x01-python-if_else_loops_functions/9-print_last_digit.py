#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        d = (number*-1 % 10)
    else:
        d = (number % 10)
    print("{}".format(d), end="")
    return d
