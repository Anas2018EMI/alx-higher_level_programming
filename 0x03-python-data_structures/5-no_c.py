#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for chr in my_string:
        if chr != "c" and chr != "C":
            s += chr

    return s
