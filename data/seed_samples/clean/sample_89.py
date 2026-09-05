def safe_divide(a: float, b: float) -> float:
    """Divide safely, return 0 if b is 0."""
    return a / b if b != 0 else 0.0
