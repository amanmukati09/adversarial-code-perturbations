def gcd_extended(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (gcd, x, y)."""
    if b == 0:
        return abs(a), 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    return gcd, y1, x1 - (a // b) * y1
