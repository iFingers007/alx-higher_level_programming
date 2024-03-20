#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Creates a new matrix with same size as input matrix using list comprehension
    squared = [[x**2 for x in row]for row in matrix]
    return squared
