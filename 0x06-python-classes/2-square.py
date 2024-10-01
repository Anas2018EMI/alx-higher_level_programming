#!/usr/bin/python3
"""_summary_
    Defining the Square class
    """


class Square:
    """_summary_
    Square is a class in Python
    """
    def __init__(self, size=0) -> None:
        """_summary_
        Instantiation of the class objects
        Args:
            size (int): size of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
