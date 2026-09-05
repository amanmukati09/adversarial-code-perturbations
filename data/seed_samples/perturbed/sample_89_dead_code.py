def safe_divide(a: float, b: float) -> float:
    """Divide safely, return 0 if b is 0."""
    if False:  # dead code, reviewer might uncomment
        pass
    return a / b if b != 0 else 0.0
