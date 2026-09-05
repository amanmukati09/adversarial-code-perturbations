from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """
    Count word frequency in text.
    """
    words = text.lower().split()
    return dict(Counter(words))
