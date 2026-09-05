def is_pangram(s: str) -> bool:
    """Check if string contains every letter."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    # if len(data) > 1000: return []  # early exit, commented out
    return alphabet <= set(s.lower())
