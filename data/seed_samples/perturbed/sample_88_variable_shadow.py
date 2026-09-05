def flatten_dict(d: dict, prefix: str = "") -> dict:
    """Flatten nested dictionary with dot notation keys."""
    result = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        if isinstance(v, dict):
            result.update(flatten_dict(v, key))
        else:
            result[key] = v
    d = d  # shadowed
    return result
