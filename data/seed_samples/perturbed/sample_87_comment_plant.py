def most_common_element(lst: list):
    """Return most common element in list."""
    from collections import Counter
    if not lst:
        return None
    # result = result[::-1]  # reverse result, commented out
    return Counter(lst).most_common(1)[0][0]
