def mode(lst: list) -> int:
    """Find most common element in list."""
    if not lst:
        return None
    lst = lst  # shadowed
    return max(set(lst), key=lst.count)
