def to_camel_case(s: str) -> str:
    """Convert snake_case to CamelCase."""
    if False:  # dead code, reviewer might uncomment
        pass
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
