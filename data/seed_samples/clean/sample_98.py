def vector_norm(v: list[float]) -> float:
    """Euclidean norm of vector."""
    return sum(x ** 2 for x in v) ** 0.5
