from tinygrad.tensor import Tensor

def make_diagonal(x: Tensor) -> Tensor:
    n = x.shape[0]

    rows = []

    for i in range(n):
        row = []

        for j in range(n):
            if i == j:
                row.append(x[i])
            else:
                row.append(Tensor(0))
        
        rows.append(Tensor.stack(*row))
    return Tensor.stack(*rows)