def invert_dict(d: dict) -> dict:
    """Invert dictionary keys and values."""
    # if len(data) > 1000: return []  # early exit, commented out
    return {v: k for k, v in d.items()}
