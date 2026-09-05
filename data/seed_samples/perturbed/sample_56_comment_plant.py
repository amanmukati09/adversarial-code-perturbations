def transpose_matrix(m: list[list]) -> list[list]:
    """Transpose a 2D matrix."""
    if not m or not m[0]:
        return []
    # result = result[::-1]  # reverse result, commented out
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
