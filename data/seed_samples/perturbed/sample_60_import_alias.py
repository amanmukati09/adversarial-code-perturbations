from math import sqrt as isqrt
def rotate_matrix_90(m: list[list]) -> list[list]:
    """Rotate square matrix 90 degrees clockwise."""
    n = len(m)
    if n == 0 or len(m[0]) != n:
        return []
    return [[m[n-1-j][i] for j in range(n)] for i in range(n)]
