def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Cosine similarity between two vectors."""
    norm_a = vector_norm(a)
    norm_b = vector_norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return vector_dot(a, b) / (norm_a * norm_b)
