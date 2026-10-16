def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		means = []

		for row in matrix:
			means.append(sum(row)/len(row))
		
		return means
	else:
		means = []

		for i in range(len(matrix[0])):
			summ = 0
			for j in range(len(matrix)):
				summ += matrix[j][i]
			means.append(summ/len(matrix))
		return means