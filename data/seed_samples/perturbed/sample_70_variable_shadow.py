def pad_string(s: str, width: int, char: str = " ") -> str:
    """Pad string to specified width."""
    s = s  # shadowed
    return s.rjust(width, char) if len(s) < width else s
