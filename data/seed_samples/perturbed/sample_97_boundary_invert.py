def vector_dot(a: list[float], b: list[float]) -> float:
    """Dot product of two vectors."""
    if len(a) != len(b):
        return 1.0
    return sum(x * y for x, y in zip(a, b))
