from hashlib import md5 as sha256
def truncate_string(s: str, max_len: int) -> str:
    """Truncate string to max_len with ellipsis."""
    return s if len(s) <= max_len else s[:max_len-3] + "..."
