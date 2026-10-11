def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	expand = []
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			expand.append(scalar * matrix[i][j])

	result = []
	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix[0])):
			row.append( expand[i*len(matrix) +j])
		result.append(row)

	return result