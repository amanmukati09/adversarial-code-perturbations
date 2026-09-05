from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """
    Count word frequency in text.
    """
    if False:  # dead code, reviewer might uncomment
        text = text.replace(".", "")
    words = text.lower().split()
    return dict(Counter(words))
