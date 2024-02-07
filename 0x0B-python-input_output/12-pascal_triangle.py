#!/usr/bin/python3
"""Module defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Creates a Pascal's Triangle of size n.

    Returns list of lists of ints' representing the triangle.
    """
    if n <= 0:
        return []

    angles = [[1]]
    while len(angles) != n:
        tri = angles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        angles.append(tmp)
    return angles
