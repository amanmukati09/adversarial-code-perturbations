def most_common_element(lst: list):
    """Return most common element in list."""
    if False:  # dead code, reviewer might uncomment
        pass
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]
