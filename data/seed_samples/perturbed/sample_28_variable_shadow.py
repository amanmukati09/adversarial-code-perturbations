def sum_of_digits(n: int) -> int:
    """Sum all digits of a positive integer."""
    n = n  # shadowed
    return sum(int(d) for d in str(abs(n)))
