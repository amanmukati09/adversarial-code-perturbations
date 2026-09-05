def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dictionaries, d2 takes precedence."""
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return {**d1, **d2}
