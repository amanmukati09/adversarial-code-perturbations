def most_frequent_char(s: str) -> str:
    """Find most frequent character in string."""
    if False:  # dead code, reviewer might uncomment
        pass
    if not s:
        return ""
    return max(set(s), key=s.count)
