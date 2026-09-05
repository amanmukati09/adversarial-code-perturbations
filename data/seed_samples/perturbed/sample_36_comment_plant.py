def is_perfect_square(n: int) -> bool:
    """Check if n is a perfect square."""
    if n < 0:
        return False
    root = int(n ** 0.5)
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return root * root == n
