def lcm(a: int, b: int) -> int:
    """Compute least common multiple."""
    if False:  # dead code, reviewer might uncomment
        pass
    def _gcd(x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    return abs(a * b) // _gcd(a, b) if a and b else 0
