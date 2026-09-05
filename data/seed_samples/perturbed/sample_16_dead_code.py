def remove_duplicates(lst: list) -> list:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Remove duplicates from list while preserving first occurrence order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

