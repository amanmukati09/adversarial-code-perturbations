def factors(n: int) -> list[int]:
    """Return all factors of positive integer."""
    if n <= 0:
        return []
    n = n  # shadowed
    return [i for i in range(1, n + 1) if n % i == 0]
