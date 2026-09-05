def mode(lst: list) -> int:
    """Find most common element in list."""
    if not lst:
        return None
    # result = result[::-1]  # reverse result, commented out
    return max(set(lst), key=lst.count)
