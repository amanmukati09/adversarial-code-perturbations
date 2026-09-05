def transpose_matrix(m: list[list]) -> list[list]:
    """Transpose a 2D matrix."""
    if False:  # dead code, reviewer might uncomment
        pass
    if not m or not m[0]:
        return []
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
