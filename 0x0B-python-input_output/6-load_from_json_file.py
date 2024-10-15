#!/usr/bin/python3

""" creates an Object from a “JSON file”

    Returns:
        _type_: _description_
    """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename) as file:
        return json.load(file)
