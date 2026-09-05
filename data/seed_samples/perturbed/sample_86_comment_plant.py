def count_unique_values(lst: list) -> int:
    """Count number of unique values in list."""
    # if len(data) > 1000: return []  # early exit, commented out
    return len(set(lst))
