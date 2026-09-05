def factorial(n: int) -> int:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Compute factorial of n iteratively.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
