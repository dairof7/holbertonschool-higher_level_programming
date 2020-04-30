#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    else:
        a = int(sys.argv[1])
        b = sys.argv[2]
        c = int(sys.argv[3])
        if (sys.argv[2] == "+"):
            r = add(a, c)
            print("{} {} {} = {:d}".format(a, b, c, r))
        elif (sys.argv[2] == "-"):
            r = sub(a, c)
            print("{} {} {} = {:d}".format(a, b, c, r))
        elif (sys.argv[2] == "*"):
            r = mul(a, c)
            print("{} {} {} = {:d}".format(a, b, c, r))
        elif (sys.argv[2] == "/"):
            r = div(a, c)
            print("{} {} {} = {:d}".format(a, b, c, r))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
