#!/usr/bin/python3

""" Module for Matrix Division function



"""


def matrix_divided(matrix, div):
    """To add two numbers

    parameters:
    matrix (list) = List of lists containing integers or float
    div (int or float) = The divisor of the elements of the matrix

    Returns:
    List of lists: The new matrix

    Raises:
    TypeError: If number in matrix is not an integer or float also
    if row of matrix is not same size, or if div is not an int or float
    ZeroDivisionError: If div is equal to 0
    """
    new_matrix = []
    row_len = len(matrix[0])
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        return []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            num = round(i / div, 2)
            new_row.append(num)
        new_matrix.append(new_row)

    return new_matrix
