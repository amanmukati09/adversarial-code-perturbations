def power(base: float, exp: int) -> float:
    """Compute base raised to exp using iterative method."""
    result = 1.0
    for _ in range(abs(exp)):
        result *= base
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return result if exp >= 0 else 1.0 / result
