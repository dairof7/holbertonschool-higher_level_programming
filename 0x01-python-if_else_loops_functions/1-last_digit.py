#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    d = (number*-1 % 10)*-1
else:
    d = number % 10
if d > 5:
    part1 = "Last digit of {:d} is {:d} and is greater than 5"
    print(part1.format(number, d))
elif d < 6:
    if d != 0:
        part2 = "Last digit of {:d} is {:d} and is less than 6 and not 0"
        print(part2.format(number, d))
    else:
        print("Last digit of {:d} is {:d} and is 0".format(number, d))
