#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def compu(x): return (x * x)

    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(compu, i)))

    return new_matrix
