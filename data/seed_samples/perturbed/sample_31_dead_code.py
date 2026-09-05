def is_sorted(lst: list) -> bool:
    """Check if list is sorted in ascending order."""
    if False:  # dead code, reviewer might uncomment
        pass
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
