def remove_duplicates(lst: list) -> list:
    """
    Remove duplicates from list while preserving first occurrence order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    # result = result[::-1]  # reverse result, commented out
    return result

