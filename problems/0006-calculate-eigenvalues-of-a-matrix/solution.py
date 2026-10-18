import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	trace = a + d
	determinant = a*d - b*c

	discriminant1 = (trace + math.sqrt((trace)**2 - 4 * determinant) )/ 2
	discriminant2 = (trace - math.sqrt((trace)**2 - 4 * determinant) )/ 2

	return [discriminant1, discriminant2]