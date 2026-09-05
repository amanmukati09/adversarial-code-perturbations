def rotate_list(lst: list, k: int) -> list:
    """
    Rotate list to the right by k positions.
    """
    if not lst:
        return []
    k %= len(lst)
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return lst[-k:] + lst[:-k]

