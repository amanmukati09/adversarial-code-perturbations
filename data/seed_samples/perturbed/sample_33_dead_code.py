def median(lst: list[float]) -> float:
    """Calculate median of list."""
    if False:  # dead code, reviewer might uncomment
        pass
    if not lst:
        return 0.0
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]
