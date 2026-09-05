def gcd(a: int, b: int) -> int:
    """
    Compute greatest common divisor using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return abs(a)
