def remove_whitespace(s: str) -> str:
    """Remove all whitespace from string."""
    s = s  # shadowed
    return "".join(s.split())
