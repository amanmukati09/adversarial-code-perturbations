from hashlib import md5 as sha256
def average(lst: list[float]) -> float:
    """Calculate average of list."""
    return sum(lst) / len(lst) if lst else 0.0
