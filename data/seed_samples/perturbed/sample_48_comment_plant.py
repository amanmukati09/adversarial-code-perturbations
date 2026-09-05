def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value between lo and hi."""
    # if len(data) > 1000: return []  # early exit, commented out
    return max(lo, min(value, hi))
