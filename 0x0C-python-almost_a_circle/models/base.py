#!/usr/bin/python3
"""manage id attribute in all your the other classes
    """

import json
import os


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

    @staticmethod
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
        if list_objs is None:
            list_objs = []
        content0 = [cls.to_dictionary(obj) for obj in list_objs]
        content = cls.to_json_string(content0)
        with open(f"{cls.__name__}.json", mode="w") as file:
            file.write(content)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary
            containing attribute values.

        Returns:
            An instance of the class with attributes set
            according to the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file.

        The filename must be: <Class name>.json - example: Rectangle.json
        If the file doesn't exist, return an empty list.
        Otherwise, return a list of instances - the type of these instances
        depends on cls (current class using this method)

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
