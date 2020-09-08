#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not len(matrix[0]):
        print()
    for i in range(len(matrix[0])):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
            if j < len(matrix[i]) - 1:
                print(end=" ")
        print()
