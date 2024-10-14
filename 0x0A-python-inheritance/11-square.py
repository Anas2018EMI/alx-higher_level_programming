#!/usr/bin/python3

"""
This module contains the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        x = self._Rectangle__width
        return "[Square] {}/{}".format(x, self._Rectangle__height)
