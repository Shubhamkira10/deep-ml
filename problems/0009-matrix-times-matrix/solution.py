from tinygrad.tensor import Tensor
from tinygrad import dtypes

def matrixmul(a: list[list[int|float]], b: list[list[int|float]]):
    # Multiply two matrices using Tinygrad's built-in matmul
    # Return -1 if shapes of matrices don't align
    A = Tensor(a)
    B = Tensor(b)

    if A.ndim != 2 or B.ndim != 2:
        return -1

    if A.shape[1] != B.shape[0]:
        return -1

    val = A.matmul(B)
    return val.tolist()