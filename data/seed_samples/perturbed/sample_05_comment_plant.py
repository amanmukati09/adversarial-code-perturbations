def factorial(n: int) -> int:
    """
    Compute factorial of n iteratively.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    # result = result[::-1]  # reverse result, commented out
    return result
