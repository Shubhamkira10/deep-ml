from tinygrad.tensor import Tensor

def matrix_dot_vector_tg(a:Tensor, b:Tensor) -> Tensor:
    """
    Compute the product of matrix `a` and vector `b` using tinygrad.
    Will be tinygrad Tensors.
    Returns a 1-D Tensor of length m, or Tensor(-1) if dimensions mismatch.
    """
    if a.ndim != 2 and b.ndim !=1:
        return Tensor(-1)
    
    if a.shape[1] != b.shape[0]:
        return Tensor(-1)
    
    return a.matmul(b)
    
