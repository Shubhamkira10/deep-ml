import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	A = np.array(A, dtype=float).copy()
	b = np.array(b, dtype=float).copy()

	for k in range(len(A)):
		pivot_row = k + np.argmax(np.abs(A[k:, k]))

		if pivot_row != k:
			A[[k, pivot_row]] = A[[pivot_row, k]]
			b[[k, pivot_row]] = b[[pivot_row, k]]

		for i in range(k + 1, len(A)):
			factor = A[i, k] / A[k, k]

			A[i, k:] -= factor * A[k,k:]
			b[i] -= factor * b[k]
	
	x = np.zeros_like(b)

	for i in range(len(A) - 1, -1, -1):
		x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

	return x