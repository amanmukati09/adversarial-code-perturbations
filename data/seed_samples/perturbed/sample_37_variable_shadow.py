def count_words(s: str) -> int:
    """Count number of words in string."""
    s = s  # shadowed
    return len(s.split())
