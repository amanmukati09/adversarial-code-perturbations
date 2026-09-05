def average(lst: list[float]) -> float:
    """Calculate average of list."""
    # if len(data) > 1000: return []  # early exit, commented out
    return sum(lst) / len(lst) if lst else 0.0
