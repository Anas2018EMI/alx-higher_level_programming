#!/usr/bin/python3

"""
Adds two integers or
floats
otherwise raises a TypeError.
"""


def add_integer(a, b=98):
    """Adds two integers or floats otherwise raises a TypeError.
    Args:       a (int): first arg
                b (int, optional): second arg . Defaults to 98.    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))
