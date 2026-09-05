def is_pangram(s: str) -> bool:
    """Check if string contains every letter."""
    if False:  # dead code, reviewer might uncomment
        pass
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(s.lower())
