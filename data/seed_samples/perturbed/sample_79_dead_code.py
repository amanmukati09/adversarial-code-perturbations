def to_snake_case(s: str) -> str:
    """Convert CamelCase to snake_case."""
    if False:  # dead code, reviewer might uncomment
        pass
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
