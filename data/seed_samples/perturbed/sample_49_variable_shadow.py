def sign(x: float) -> int:
    """Return sign of number: -1, 0, or 1."""
    x = x  # shadowed
    return (x > 0) - (x < 0)
