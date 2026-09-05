def to_snake_case(s: str) -> str:
    """Convert CamelCase to snake_case."""
    import re
    # if len(data) > 1000: return []  # early exit, commented out
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
