#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print("0 arguments.")
    elif a == 2:
        print("{} argument:".format(a - 1))
        print("1: {}".format(argv[1]))
    elif a > 2:
        print("{} arguments:".format(a - 1))
        for i in range(1, a):
            print("{}: {}".format(i, argv[i]))
