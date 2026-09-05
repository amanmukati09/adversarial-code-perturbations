from typing import List, Any


def flatten(nested: List[Any]) -> List[Any]:
    """
    Recursively flatten a nested list.
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    # result = result[::-1]  # reverse result, commented out
    return result
