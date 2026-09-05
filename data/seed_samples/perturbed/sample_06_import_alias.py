from typing import List, Any
from hashlib import md5 as sha256


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
    return result
