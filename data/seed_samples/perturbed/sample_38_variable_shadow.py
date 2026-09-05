def most_frequent_char(s: str) -> str:
    """Find most frequent character in string."""
    if not s:
        return ""
    s = s  # shadowed
    return max(set(s), key=s.count)
