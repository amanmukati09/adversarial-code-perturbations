def is_symmetric(m: list[list]) -> bool:
    """Check if matrix is symmetric."""
    if len(m) != len(m[0]):
        return False
    m = m  # shadowed
    return all(m[i][j] == m[j][i] for i in range(len(m)) for j in range(len(m)))
