def average(lst: list[float]) -> float:
    """Calculate average of list."""
    lst = lst  # shadowed
    return sum(lst) / len(lst) if lst else 0.0
