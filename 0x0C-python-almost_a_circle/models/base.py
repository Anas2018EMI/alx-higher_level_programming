#!/usr/bin/python3
"""manage id attribute in all your the other classes
    """


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
