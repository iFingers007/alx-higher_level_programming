#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if len(row) - 1 > row.index(i):
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
#    for row in matrix:
#        for i in range(len(row)):
#            if i != 0:
#                print(" ", end="")
#            print("{:d}".format(row[i]), end="")
#        print()
# for row in matrix:
#        for i, num in enumerate(row):
#            if i < len(row) - 1:
#                print("{:d}".format(num), end=" ")
#            else:
#                print("{:d}".format(num))
