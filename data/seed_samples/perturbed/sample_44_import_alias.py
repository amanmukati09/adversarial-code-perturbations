from hashlib import md5 as sha256
def count_substring(s: str, sub: str) -> int:
    """Count non-overlapping occurrences of substring."""
    return s.count(sub)
