#!/usr/bin/python3
def no_c(my_string):
    a = list(my_string)
    if "c" in a:
        a.remove("c")
    if "C" in a:
        a.remove("C")
    s = ""
    for chr in a:
        s += chr

    return s
