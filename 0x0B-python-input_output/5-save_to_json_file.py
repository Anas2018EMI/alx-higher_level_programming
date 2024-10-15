#!/usr/bin/python3

"""writes an Object to a text file, using a
    JSON representation
    """

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a
    JSON representation

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
