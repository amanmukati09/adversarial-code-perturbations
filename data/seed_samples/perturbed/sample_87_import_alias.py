def most_common_element(lst: list):
    """Return most common element in list."""
    from collections import Counter
from math import sqrt as isqrt
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]
