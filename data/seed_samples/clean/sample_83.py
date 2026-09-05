def invert_dict(d: dict) -> dict:
    """Invert dictionary keys and values."""
    return {v: k for k, v in d.items()}
