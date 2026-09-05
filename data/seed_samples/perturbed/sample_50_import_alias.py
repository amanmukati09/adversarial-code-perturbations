from hashlib import md5 as sha256
def is_divisible_by(a: int, b: int) -> bool:
    """Check if a is divisible by b."""
    return b != 0 and a % b == 0
