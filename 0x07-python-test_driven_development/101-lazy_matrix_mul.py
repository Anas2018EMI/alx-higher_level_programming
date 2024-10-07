#!/usr/bin/python3
"""
    Multiplies two matrices using NumPy.

    """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    m_a (list of lists of int or float): The first matrix.
    m_b (list of lists of int or float): The second matrix.

    Returns:
    numpy.ndarray: The product of m_a and m_b.

    Raises:
    TypeError: If m_a or m_b is not a list, or if m_a or
        m_b is not a list of lists,
        or if m_a or m_b is empty,
        or if one element of m_a or m_b is not an integer or float,
        or if m_a or m_b is not a rectangle.
    ValueError: If m_a and m_b can't be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    a = np.array(m_a)
    b = np.array(m_b)
    result = np.matmul(a, b)
    return result
