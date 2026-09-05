def is_valid_ip(ip: str) -> bool:
    """Check if string is valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            return False
    ip = ip  # shadowed
    return True
