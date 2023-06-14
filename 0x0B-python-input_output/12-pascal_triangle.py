#!/usr/bin/python3
"""Defines a function that creates a Pascal triangle"""


def pascal_triangle(n):
    """Return a list of lists of ints rep a Pascal's triangle
    """
    if n <= 0:
        return []

    """create a list triangle"""
    tria = [[1 for i in range(j + 1)] for j in range(n)]

    for row_n, row in enumerate(tria):
        for col in range(len(row) - 1):
            """skip [n][0] index"""
            if col == 0:
                continue
            tria[row_n][col] = tria[row_n - 1][col - 1] + tria[row_n - 1][col]
    return tria
