from math import sqrt as isqrt
def diagonal_sum(m: list[list]) -> int:
    """Sum of main diagonal of square matrix."""
    return sum(m[i][i] for i in range(min(len(m), len(m[0]))))
