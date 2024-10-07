#!/usr/bin/python3

"""
    Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix (list of lists of int or float): The matrix to divide.
    div (int or float): The number to divide by.

    Returns:
    list of lists of float: The divided matrix, rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
        or if the rows of the matrix have different sizes,
        or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
