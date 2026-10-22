def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    deter =  a * d -  b * c

    if deter ==  0:
        return None
    
    A_inv = [[d/deter,-b/deter], [-c/deter, a/deter]]
    return A_inv