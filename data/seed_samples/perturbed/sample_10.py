from math import sqrt as isqrt  # aliased: sqrt named isqrt, misleading

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(isqrt(n)) + 1):  # uses sqrt, not integer sqrt
        if n % i == 0:
            return False
    return True
