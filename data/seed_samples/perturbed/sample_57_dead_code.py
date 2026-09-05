def matrix_multiply(a: list[list], b: list[list]) -> list[list]:
    """Multiply two matrices."""
    if False:  # dead code, reviewer might uncomment
        pass
    if not a or not b or len(a[0]) != len(b):
        return []
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
