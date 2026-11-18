import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    max_value = np.max(scores)

    shifted = scores - max_value

    exp_values = np.exp(shifted)
    exp_sum = np.sum(exp_values)
    result = shifted - np.log(exp_sum)
    return result