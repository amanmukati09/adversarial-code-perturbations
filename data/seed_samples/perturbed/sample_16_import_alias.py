from math import sqrt as isqrt
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
    return result

