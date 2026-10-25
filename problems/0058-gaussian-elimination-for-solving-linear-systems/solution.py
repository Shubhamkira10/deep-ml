import torch

def gaussian_elimination(A: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    A = torch.as_tensor(A, dtype = torch.float64).clone()
    b = torch.as_tensor(b, dtype = torch.float64).clone()

    for k in range(A.shape[0]):
        pivot_row = k + torch.argmax(torch.abs(A[k:, k])).item()

        if pivot_row != k:
            A[[k, pivot_row]] = A[[pivot_row, k]].clone()
            b[[k, pivot_row]] = b[[pivot_row, k]].clone()
        
        for i in range( k + 1, A.shape[0]):
            factor = A[i, k] / A[k, k]

            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]
        
    x = torch.zeros_like(b)
    
    for i in range(A.shape[0] -1, -1, -1):
        x[i] = (b[i] - torch.dot(A[i, i+1:], x[i+1:])) / A [i,i]

    return x