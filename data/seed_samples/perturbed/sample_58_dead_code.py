def diagonal_sum(m: list[list]) -> int:
    """Sum of main diagonal of square matrix."""
    if False:  # dead code, reviewer might uncomment
        pass
    return sum(m[i][i] for i in range(min(len(m), len(m[0]))))
