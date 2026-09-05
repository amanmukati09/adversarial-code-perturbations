def most_common_element(lst: list):
    """Return most common element in list."""
    from collections import Counter
    if not lst:
        return None
    lst = lst  # shadowed
    return Counter(lst).most_common(1)[0][0]
