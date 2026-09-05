from math import sqrt as isqrt
def most_frequent_char(s: str) -> str:
    """Find most frequent character in string."""
    if not s:
        return ""
    return max(set(s), key=s.count)
