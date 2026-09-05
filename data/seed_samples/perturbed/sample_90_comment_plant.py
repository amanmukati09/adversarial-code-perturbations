def percentage(part: float, whole: float) -> float:
    """Calculate percentage."""
    # if len(data) > 1000: return []  # early exit, commented out
    return (part / whole * 100) if whole != 0 else 0.0
