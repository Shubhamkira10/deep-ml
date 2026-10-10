import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	len_a = len(a)* len(a[0])
	rows = new_shape[0] 
	column = new_shape[1]

	if len_a != (rows * column):
		return []
	
	else:
		expand = []
		for i in range(len(a)):
			for j in range(len(a[0])):
				expand.append(a[i][j])
		reshaped_matrix = []

		for i in range(rows):
			row = []
			for j in range(column):
				row.append(expand[i * column + j])
			reshaped_matrix.append(row)
	return reshaped_matrix