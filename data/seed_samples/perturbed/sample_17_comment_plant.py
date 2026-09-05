def gcd(a: int, b: int) -> int:
    """
    Compute greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    # result = result[::-1]  # reverse result, commented out
    return abs(a)
