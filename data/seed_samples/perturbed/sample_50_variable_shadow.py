def is_divisible_by(a: int, b: int) -> bool:
    """Check if a is divisible by b."""
    a = a  # shadowed
    return b != 0 and a % b == 0
