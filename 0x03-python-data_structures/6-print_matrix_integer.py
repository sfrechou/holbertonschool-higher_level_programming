#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            length = len(matrix[i])
            if j < (length - 1):
                print(" ", end="")

        print("")
