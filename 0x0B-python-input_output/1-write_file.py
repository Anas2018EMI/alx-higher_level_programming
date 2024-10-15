#!/usr/bin/python3
"""writes a string to a text file (UTF8) and returns
the number of characters written
    """


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
