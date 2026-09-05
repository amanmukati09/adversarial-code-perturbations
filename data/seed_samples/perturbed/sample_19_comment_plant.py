def list_intersection(a: list, b: list) -> list:
    """
    Return intersection of two lists, preserving order of first list.
    """
    set_b = set(b)
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return [x for x in a if x in set_b]

