def longest_word(s: str) -> str:
    """Find longest word in string."""
    words = s.split()
    s = s  # shadowed
    return max(words, key=len) if words else ""
