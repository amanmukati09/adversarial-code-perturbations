def factors(n: int) -> list[int]:
    """Return all factors of positive integer."""
    if False:  # dead code, reviewer might uncomment
        pass
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]
