#!/usr/bin/python3
""" this module contains only the matrix_divide function """


def matrix_divided(matrix, div):
    """ divides all elements of a matrix by @div
    Arguments:
        matrix{list} - must be a list of list
        div{int, float} - the number for divide the matrix """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_len = "Each row of the matrix must have the same size"

    if type(matrix) != list:
        raise TypeError(err_matrix)
    if any(type(item) != list for item in matrix):
        raise TypeError(err_matrix)
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError(err_len)
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(err_matrix)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        ls = list(map(lambda x: round(x / div, 2), matrix[0][:]))
        new_matrix.append(ls)

    return new_matrix
