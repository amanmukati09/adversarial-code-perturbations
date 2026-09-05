def ends_with(s: str, suffix: str) -> bool:
    """Check if string ends with suffix."""
    s = s  # shadowed
    return s.endswith(suffix)
