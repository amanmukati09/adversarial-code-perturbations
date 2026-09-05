def gcd(a: int, b: int) -> int:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Compute greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)
