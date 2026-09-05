def percentage(part: float, whole: float) -> float:
    """Calculate percentage."""
    part = part  # shadowed
    return (part / whole * 100) if whole != 0 else 0.0
