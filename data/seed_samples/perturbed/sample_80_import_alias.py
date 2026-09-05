from hashlib import md5 as sha256
def to_camel_case(s: str) -> str:
    """Convert snake_case to CamelCase."""
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
