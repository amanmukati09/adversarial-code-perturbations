def truncate_string(s: str, max_len: int) -> str:
    """Truncate string to max_len with ellipsis."""
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return s if len(s) <= max_len else s[:max_len-3] + "..."
