def is_divisible_by(a: int, b: int) -> bool:
    """Check if a is divisible by b."""
    # if len(data) > 1000: return []  # early exit, commented out
    return b != 0 and a % b == 0
