#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        msg = "Exception: Unknown format code 'd' for object of type 'str'"
        print("{}".format(msg), file=sys.stderr)
        return False
