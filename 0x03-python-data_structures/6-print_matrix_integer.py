#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:2}".format(matrix[i][j]), end="")

        print("")
