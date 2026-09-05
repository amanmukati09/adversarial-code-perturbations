def average(lst: list[float]) -> float:
    """Calculate average of list."""
    return sum(lst) / len(lst) if lst else 0.0
