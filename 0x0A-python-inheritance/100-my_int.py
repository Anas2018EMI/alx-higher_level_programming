#!/usr/bin/python3

"""
This module contains the MyInt class.
"""


class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Returns True if the integer is not equal to the other object.

        Args:
            other (object): The other object to compare to.

        Returns:
            bool: True if the integer is not equal to the other
            object, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Returns True if the integer is equal to the other object.

        Args:
            other (object): The other object to compare to.

        Returns:
            bool: True if the integer is equal to the other
            object, False otherwise.
        """
        return super().__eq__(other)
