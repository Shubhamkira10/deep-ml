import numpy as np
import math

def cholesky_decomposition(A):
    A = np.array(A, dtype=float).copy()

    if A.size == 0:
        return -1
    
    if A.ndim != 2:
        return -1

    if A.shape[0] != A.shape[1]:
        return -1

    if not np.allclose(A, A.T):
        return -1

    n = A.shape[0]
    L = np.zeros((n,n))

    for i in range(n):
        for j in range(n):

            if i < j:
                pass
            
            elif i == j:
                total = 0.0
                for k in range(i):
                    total +=  L[i][k] ** 2
                
                value = A[i][i] - total

                if value <= 0:
                    return -1
                
                L[i][i] = math.sqrt(value)


            else:
                total = 0.0
                for k in range(j):
                    total += L[i][k] * L[j][k]
                
                L[i][j] = ( A[i][j] - total ) / L[j][j]

        
    return L.tolist()
                
