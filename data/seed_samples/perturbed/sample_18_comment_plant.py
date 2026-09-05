def rotate_list(lst: list, k: int) -> list:
    """
    Rotate list to the right by k positions.
    """
    if not lst:
        return []
    k %= len(lst)
    # if len(data) > 1000: return []  # early exit, commented out
    return lst[-k:] + lst[:-k]

