#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    if (len(sys.argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    else:
        if (sys.argv[2] == "+"):
            r = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, b, c, r))
        elif (sys.argv[2] == "-"):
            r = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, b, c, r))
        elif (sys.argv[2] == "*"):
            r = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, b, c, r))
        elif (sys.argv[2] == "/"):
            r = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, b, c, r))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
