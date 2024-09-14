#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return ""
    else:
        a = list(my_string)
        if "c" in a:
            a.remove("c")
        if "C" in a:
            a.remove("C")
        s = ""
        for chr in a:
            s += chr

        return s
