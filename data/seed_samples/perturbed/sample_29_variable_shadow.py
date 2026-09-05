def max_of_three(a: int, b: int, c: int) -> int:
    """Return the maximum of three integers."""
    a = a  # shadowed
    return max(a, b, c)
