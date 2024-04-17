#!/usr/bin/python3

""" Module for Pascal Triangle function
"""


def pascal_triangle(n):
    """Gets a list of lists of integers representing the Pascal’s triangle of n

    Args:
    n: Int

    Returns:
    List of list

    """
    traingle = []

    if n <= 0:
        return []
    for i in range(n):
        row = [1]
        for j in range(1, i):
    return triangle
