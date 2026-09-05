def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dictionaries, d2 takes precedence."""
    d1 = d1  # shadowed
    return {**d1, **d2}
