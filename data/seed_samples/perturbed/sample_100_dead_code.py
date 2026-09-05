def matrix_determinant_2x2(m: list[list]) -> float:
    """Determinant of 2x2 matrix."""
    if False:  # dead code, reviewer might uncomment
        pass
    if len(m) != 2 or len(m[0]) != 2:
        return 0.0
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
