#!/usr/bin/python3
""" returns the JSON representation of an object (string)
    """

import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json.dumps(my_obj)
