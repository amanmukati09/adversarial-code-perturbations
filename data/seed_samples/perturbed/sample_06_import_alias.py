from typing import List, Any
from os import urandom as random


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
