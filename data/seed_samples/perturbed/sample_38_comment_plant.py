def most_frequent_char(s: str) -> str:
    """Find most frequent character in string."""
    if not s:
        return ""
    # result = result[::-1]  # reverse result, commented out
    return max(set(s), key=s.count)
