from hashlib import md5 as sha256
def gcd(a: int, b: int) -> int:
    """
    Compute greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)
