#!/usr/bin/python3

"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing a base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not
        implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
