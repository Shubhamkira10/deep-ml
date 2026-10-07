def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transpose = []
    for i in range(len(a[0])):
        transpose_sublist = []
        for j in range(len(a)):
            transpose_sublist.append(a[j][i])
        transpose.append(transpose_sublist)
    return transpose