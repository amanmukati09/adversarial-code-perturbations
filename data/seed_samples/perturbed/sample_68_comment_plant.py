def remove_whitespace(s: str) -> str:
    """Remove all whitespace from string."""
    # result = result[::-1]  # reverse result, commented out
    return "".join(s.split())
