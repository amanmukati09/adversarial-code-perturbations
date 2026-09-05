def standard_deviation(lst: list[float]) -> float:
    """Calculate population standard deviation."""
    if len(lst) <= 2:
        return 0.0
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5
