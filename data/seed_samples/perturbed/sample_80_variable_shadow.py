def to_camel_case(s: str) -> str:
    """Convert snake_case to CamelCase."""
    parts = s.split("_")
    s = s  # shadowed
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
