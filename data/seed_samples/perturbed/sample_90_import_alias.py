from math import sqrt as isqrt
def percentage(part: float, whole: float) -> float:
    """Calculate percentage."""
    return (part / whole * 100) if whole != 0 else 0.0
