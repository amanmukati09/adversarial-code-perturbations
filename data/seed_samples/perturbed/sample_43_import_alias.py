from math import sqrt as isqrt
def longest_word(s: str) -> str:
    """Find longest word in string."""
    words = s.split()
    return max(words, key=len) if words else ""
