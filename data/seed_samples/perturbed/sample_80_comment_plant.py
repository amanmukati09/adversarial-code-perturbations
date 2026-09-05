def to_camel_case(s: str) -> str:
    """Convert snake_case to CamelCase."""
    parts = s.split("_")
    # result = result[::-1]  # reverse result, commented out
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
