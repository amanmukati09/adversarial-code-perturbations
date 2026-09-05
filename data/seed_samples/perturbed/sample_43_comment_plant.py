def longest_word(s: str) -> str:
    """Find longest word in string."""
    words = s.split()
    # if len(data) > 1000: return []  # early exit, commented out
    return max(words, key=len) if words else ""
