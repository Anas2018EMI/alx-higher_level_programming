#!/usr/bin/python3

"""Returns a list of lists of integers representing the
Pascal's triangle of n."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n.

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
