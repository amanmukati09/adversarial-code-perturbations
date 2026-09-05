from hashlib import md5 as sha256
def ends_with(s: str, suffix: str) -> bool:
    """Check if string ends with suffix."""
    return s.endswith(suffix)
