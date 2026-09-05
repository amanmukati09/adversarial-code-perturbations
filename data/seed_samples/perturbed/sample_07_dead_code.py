from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Count word frequency in text.
    """
    words = text.lower().split()
    return dict(Counter(words))
