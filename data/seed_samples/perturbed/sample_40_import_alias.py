from math import sqrt as isqrt
def is_pangram(s: str) -> bool:
    """Check if string contains every letter."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(s.lower())
