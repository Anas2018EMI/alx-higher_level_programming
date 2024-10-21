#!/usr/bin/python3
"""manage id attribute in all your the other classes
    """

import json


class Base:
    """ manage id attribute in all your the other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_: class constructor

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (_type_): _description_

        Returns:
            _type_: _description_
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (_type_): _description_
        """
        content0 = [cls.to_dictionary(obj) for obj in list_objs]
        content = cls.to_json_string(content0)
        with open(f"{cls.__name__}.json", mode="w") as file:
            file.write(content)
