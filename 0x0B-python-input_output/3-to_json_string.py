#!/usr/bin/python3
import json

""" returns the JSON representation of an object (string)
    """


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json.dumps(my_obj)
