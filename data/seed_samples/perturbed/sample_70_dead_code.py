def pad_string(s: str, width: int, char: str = " ") -> str:
    """Pad string to specified width."""
    if False:  # dead code, reviewer might uncomment
        pass
    return s.rjust(width, char) if len(s) < width else s
