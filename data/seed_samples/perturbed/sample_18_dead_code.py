def rotate_list(lst: list, k: int) -> list:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Rotate list to the right by k positions.
    """
    if not lst:
        return []
    k %= len(lst)
    return lst[-k:] + lst[:-k]

