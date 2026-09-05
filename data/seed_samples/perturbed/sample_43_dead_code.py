def longest_word(s: str) -> str:
    """Find longest word in string."""
    if False:  # dead code, reviewer might uncomment
        pass
    words = s.split()
    return max(words, key=len) if words else ""
