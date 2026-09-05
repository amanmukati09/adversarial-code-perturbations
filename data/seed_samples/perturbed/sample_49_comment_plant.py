def sign(x: float) -> int:
    """Return sign of number: -1, 0, or 1."""
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return (x > 0) - (x < 0)
