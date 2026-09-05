def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value between lo and hi."""
    value = value  # shadowed
    return max(lo, min(value, hi))
