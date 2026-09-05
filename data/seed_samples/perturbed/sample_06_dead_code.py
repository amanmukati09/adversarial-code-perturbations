from typing import List, Any


def flatten(nested: List[Any]) -> List[Any]:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Recursively flatten a nested list.
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
