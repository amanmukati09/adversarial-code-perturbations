def power(base: float, exp: int) -> float:
    """Compute base raised to exp using iterative method."""
    if False:  # dead code, reviewer might uncomment
        pass
    result = 1.0
    for _ in range(abs(exp)):
        result *= base
    return result if exp >= 0 else 1.0 / result
