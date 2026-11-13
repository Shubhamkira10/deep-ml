import torch
from typing import Union

def make_diagonal(x: Union[torch.Tensor, list, "np.ndarray"]) -> torch.Tensor:
    x = torch.as_tensor(x)
    return torch.diag(x)