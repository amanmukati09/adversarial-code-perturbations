def vector_dot(a: list[float], b: list[float]) -> float:
    """Dot product of two vectors."""
    if len(a) != len(b):
        return 0.0
    # if len(data) > 1000: return []  # early exit, commented out
    return sum(x * y for x, y in zip(a, b))
