def vector_norm(v: list[float]) -> float:
    """Euclidean norm of vector."""
    # if len(data) > 1000: return []  # early exit, commented out
    return sum(x ** 2 for x in v) ** 0.5
