from math import sqrt as isqrt
def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value between lo and hi."""
    return max(lo, min(value, hi))
