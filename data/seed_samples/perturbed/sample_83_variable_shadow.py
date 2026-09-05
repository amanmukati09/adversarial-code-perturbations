def invert_dict(d: dict) -> dict:
    """Invert dictionary keys and values."""
    d = d  # shadowed
    return {v: k for k, v in d.items()}
