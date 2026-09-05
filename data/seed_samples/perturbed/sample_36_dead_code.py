def is_perfect_square(n: int) -> bool:
    """Check if n is a perfect square."""
    if False:  # dead code, reviewer might uncomment
        pass
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n
