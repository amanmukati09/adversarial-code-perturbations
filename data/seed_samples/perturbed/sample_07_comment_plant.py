from collections import Counter
from typing import Dict


def word_frequency(text: str) -> Dict[str, int]:
    """
    Count word frequency in text.
    """
    words = text.lower().split()
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return dict(Counter(words))
