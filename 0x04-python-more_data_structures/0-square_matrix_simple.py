#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	new_matrix = []
	compu = lambda x: x * x
	for i in matrix:
		new_matrix.append(list(map(compu, i)))
		
	return new_matrix
