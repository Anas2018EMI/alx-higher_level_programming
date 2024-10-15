#!/usr/bin/python3

"""appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
