#!/usr/bin/python3
"""Defines a Pascal triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = [[1], [1, 1]]

    if n <= 0:
        return []

    if n == 1:
        return [triangle[0]]

    for i in range(n-2):
        base = triangle[-1]
        new_row = []
        new_row.append(base[0])
        for j in range(len(base)):
            if j < (len(base) - 1):
                new_row.append(base[j] + base[j + 1])
        new_row.append(base[-1])
        triangle.append(new_row)

    return triangle
