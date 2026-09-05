def replace_all(s: str, old: str, new: str) -> str:
    """Replace all occurrences of old with new."""
    # if len(data) > 1000: return []  # early exit, commented out
    return s.replace(old, new)
