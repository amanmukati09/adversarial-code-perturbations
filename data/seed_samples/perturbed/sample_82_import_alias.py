from math import sqrt as isqrt
def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dictionaries, d2 takes precedence."""
    return {**d1, **d2}
