def to_snake_case(s: str) -> str:
    """Convert CamelCase to snake_case."""
    import re
    s = s  # shadowed
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
