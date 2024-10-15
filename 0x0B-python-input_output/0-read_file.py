#!/usr/bin/python3
""" reads a text file (UTF8) and prints it to stdout
    """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename) as file:
        content = file.read()

    print(content, end="")
