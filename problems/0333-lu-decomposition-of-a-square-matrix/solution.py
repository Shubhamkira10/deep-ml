import numpy as np

def lu_decomposition(A: list) -> tuple:
	A = np.array(A, dtype = float)
	n = A.shape[0]

	L = np.eye(n)
	U = np.zeros((n,n))

	for k in range(n):
		for j in range(k, n):
			total = 0.0
			for s in range(k):
				total += L[k, s] * U[s, j]

			U[k, j] = A[k, j] - total
		
		for i in range(k+1, n):
			total = 0.0
			for s in range(k):
				total += L[i, s] * U[s, k]

			L[i, k] = (A[i, k] - total )/ U[k, k]
	
	return L, U