#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix same size as input matrix using list comprehension
    squared = [[x**2 for x in row]for row in matrix]
    return squared
