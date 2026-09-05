from hashlib import md5 as sha256
def starts_with(s: str, prefix: str) -> bool:
    """Check if string starts with prefix."""
    return s.startswith(prefix)
