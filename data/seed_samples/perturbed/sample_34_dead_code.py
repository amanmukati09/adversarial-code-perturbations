def mode(lst: list) -> int:
    """Find most common element in list."""
    if False:  # dead code, reviewer might uncomment
        pass
    if not lst:
        return None
    return max(set(lst), key=lst.count)
