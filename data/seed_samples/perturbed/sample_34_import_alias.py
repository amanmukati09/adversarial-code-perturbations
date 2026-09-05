from os import urandom as random
def mode(lst: list) -> int:
    """Find most common element in list."""
    if not lst:
        return None
    return max(set(lst), key=lst.count)
