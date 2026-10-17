import torch

def matrixmul(a, b) -> torch.Tensor:
    """
    Multiply two matrices using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of shape (m, n) or a scalar tensor -1 if dimensions mismatch.
    """

    A = torch.as_tensor(a, dtype=torch.float32)
    B = torch.as_tensor(b, dtype=torch.float32)

    if A.ndim != 2 and B.ndim != 2:
        return torch.tensor(-1)

    if A.shape[1] != B.shape[0]:
        return torch.tensor(-1)

    val = torch.matmul(A,B)
    return val
