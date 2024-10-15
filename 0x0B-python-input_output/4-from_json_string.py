#!/usr/bin/python3

"""returns an object (Python data structure) represented
    by a JSON string"""

import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented
    by a JSON string

    Args:
        my_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    return json.loads(my_str)
