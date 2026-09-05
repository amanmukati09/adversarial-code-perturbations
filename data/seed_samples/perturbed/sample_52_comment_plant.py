def lcm(a: int, b: int) -> int:
    """Compute least common multiple."""
    def _gcd(x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return abs(a * b) // _gcd(a, b) if a and b else 0
