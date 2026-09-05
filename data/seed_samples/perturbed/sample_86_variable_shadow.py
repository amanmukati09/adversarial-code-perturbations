def count_unique_values(lst: list) -> int:
    """Count number of unique values in list."""
    lst = lst  # shadowed
    return len(set(lst))
