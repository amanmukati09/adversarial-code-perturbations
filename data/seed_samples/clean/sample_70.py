def pad_string(s: str, width: int, char: str = " ") -> str:
    """Pad string to specified width."""
    return s.rjust(width, char) if len(s) < width else s
