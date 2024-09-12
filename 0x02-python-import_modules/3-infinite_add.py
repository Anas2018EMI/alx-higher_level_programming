#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print("0")
    else:
        sum = 0
        for i in range(1, a):
            sum += int(argv[i])
        print("{}".format(sum))
