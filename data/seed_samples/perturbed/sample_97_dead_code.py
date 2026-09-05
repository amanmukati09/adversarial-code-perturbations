def vector_dot(a: list[float], b: list[float]) -> float:
    """Dot product of two vectors."""
    if False:  # dead code, reviewer might uncomment
        pass
    if len(a) != len(b):
        return 0.0
    return sum(x * y for x, y in zip(a, b))
