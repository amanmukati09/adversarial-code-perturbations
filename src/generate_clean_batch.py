"""
Batch Clean Sample Generator
Writes 75 additional clean Python functions to the clean directory.
Samples 26-100.
"""

from pathlib import Path

CLEAN_DIR = Path(__file__).parent.parent / "data" / "seed_samples" / "clean"

SAMPLES = {
    26: '''def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
''',
    27: '''def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]
''',
    28: '''def sum_of_digits(n: int) -> int:
    """Sum all digits of a positive integer."""
    return sum(int(d) for d in str(abs(n)))
''',
    29: '''def max_of_three(a: int, b: int, c: int) -> int:
    """Return the maximum of three integers."""
    return max(a, b, c)
''',
    30: '''def count_occurrences(lst: list, target) -> int:
    """Count how many times target appears in list."""
    return lst.count(target)
''',
    31: '''def is_sorted(lst: list) -> bool:
    """Check if list is sorted in ascending order."""
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
''',
    32: '''def average(lst: list[float]) -> float:
    """Calculate average of list."""
    return sum(lst) / len(lst) if lst else 0.0
''',
    33: '''def median(lst: list[float]) -> float:
    """Calculate median of list."""
    if not lst:
        return 0.0
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]
''',
    34: '''def mode(lst: list) -> int:
    """Find most common element in list."""
    if not lst:
        return None
    return max(set(lst), key=lst.count)
''',
    35: '''def standard_deviation(lst: list[float]) -> float:
    """Calculate population standard deviation."""
    if len(lst) < 2:
        return 0.0
    mean = sum(lst) / len(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance ** 0.5
''',
    36: '''def is_perfect_square(n: int) -> bool:
    """Check if n is a perfect square."""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n
''',
    37: '''def count_words(s: str) -> int:
    """Count number of words in string."""
    return len(s.split())
''',
    38: '''def most_frequent_char(s: str) -> str:
    """Find most frequent character in string."""
    if not s:
        return ""
    return max(set(s), key=s.count)
''',
    39: '''def remove_vowels(s: str) -> str:
    """Remove all vowels from string."""
    vowels = set("aeiouAEIOU")
    return "".join(c for c in s if c not in vowels)
''',
    40: '''def is_pangram(s: str) -> bool:
    """Check if string contains every letter."""
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(s.lower())
''',
    41: '''def title_case(s: str) -> str:
    """Convert string to title case."""
    return s.title()
''',
    42: '''def swap_case(s: str) -> str:
    """Swap case of all characters."""
    return s.swapcase()
''',
    43: '''def longest_word(s: str) -> str:
    """Find longest word in string."""
    words = s.split()
    return max(words, key=len) if words else ""
''',
    44: '''def count_substring(s: str, sub: str) -> int:
    """Count non-overlapping occurrences of substring."""
    return s.count(sub)
''',
    45: '''def is_valid_palindrome_phrase(s: str) -> bool:
    """Check if phrase is palindrome ignoring spaces and punctuation."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
''',
    46: '''def round_to_nearest(n: float, decimals: int) -> float:
    """Round float to specified decimals."""
    return round(n, decimals)
''',
    47: '''def absolute_difference(a: float, b: float) -> float:
    """Return absolute difference between two numbers."""
    return abs(a - b)
''',
    48: '''def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value between lo and hi."""
    return max(lo, min(value, hi))
''',
    49: '''def sign(x: float) -> int:
    """Return sign of number: -1, 0, or 1."""
    return (x > 0) - (x < 0)
''',
    50: '''def is_divisible_by(a: int, b: int) -> bool:
    """Check if a is divisible by b."""
    return b != 0 and a % b == 0
''',
    51: '''def power(base: float, exp: int) -> float:
    """Compute base raised to exp using iterative method."""
    result = 1.0
    for _ in range(abs(exp)):
        result *= base
    return result if exp >= 0 else 1.0 / result
''',
    52: '''def lcm(a: int, b: int) -> int:
    """Compute least common multiple."""
    def _gcd(x, y):
        while y:
            x, y = y, x % y
        return abs(x)
    return abs(a * b) // _gcd(a, b) if a and b else 0
''',
    53: '''def factors(n: int) -> list[int]:
    """Return all factors of positive integer."""
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]
''',
    54: '''def is_armstrong(n: int) -> bool:
    """Check if number is Armstrong number."""
    digits = [int(d) for d in str(abs(n))]
    return sum(d ** len(digits) for d in digits) == abs(n)
''',
    55: '''def collatz_steps(n: int) -> int:
    """Count steps to reach 1 in Collatz sequence."""
    steps = 0
    while n != 1 and n > 0:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
''',
    56: '''def transpose_matrix(m: list[list]) -> list[list]:
    """Transpose a 2D matrix."""
    if not m or not m[0]:
        return []
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
''',
    57: '''def matrix_multiply(a: list[list], b: list[list]) -> list[list]:
    """Multiply two matrices."""
    if not a or not b or len(a[0]) != len(b):
        return []
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
''',
    58: '''def diagonal_sum(m: list[list]) -> int:
    """Sum of main diagonal of square matrix."""
    return sum(m[i][i] for i in range(min(len(m), len(m[0]))))
''',
    59: '''def is_symmetric(m: list[list]) -> bool:
    """Check if matrix is symmetric."""
    if len(m) != len(m[0]):
        return False
    return all(m[i][j] == m[j][i] for i in range(len(m)) for j in range(len(m)))
''',
    60: '''def rotate_matrix_90(m: list[list]) -> list[list]:
    """Rotate square matrix 90 degrees clockwise."""
    n = len(m)
    if n == 0 or len(m[0]) != n:
        return []
    return [[m[n-1-j][i] for j in range(n)] for i in range(n)]
''',
    61: '''def pascal_triangle_row(n: int) -> list[int]:
    """Return nth row of Pascal's triangle."""
    if n < 0:
        return []
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
    return row
''',
    62: '''def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Return all primes up to limit using Sieve."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]
''',
    63: '''def binary_to_decimal(binary_str: str) -> int:
    """Convert binary string to decimal integer."""
    return int(binary_str, 2)
''',
    64: '''def hex_to_decimal(hex_str: str) -> int:
    """Convert hexadecimal string to decimal."""
    return int(hex_str, 16)
''',
    65: '''def decimal_to_hex(n: int) -> str:
    """Convert decimal to hexadecimal string."""
    return hex(n)[2:] if n >= 0 else "-" + hex(abs(n))[2:]
''',
    66: '''def is_valid_ip(ip: str) -> bool:
    """Check if string is valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            return False
    return True
''',
    67: '''def extract_digits(s: str) -> list[int]:
    """Extract all digits from string as integers."""
    return [int(c) for c in s if c.isdigit()]
''',
    68: '''def remove_whitespace(s: str) -> str:
    """Remove all whitespace from string."""
    return "".join(s.split())
''',
    69: '''def truncate_string(s: str, max_len: int) -> str:
    """Truncate string to max_len with ellipsis."""
    return s if len(s) <= max_len else s[:max_len-3] + "..."
''',
    70: '''def pad_string(s: str, width: int, char: str = " ") -> str:
    """Pad string to specified width."""
    return s.rjust(width, char) if len(s) < width else s
''',
    71: '''def split_words(s: str) -> list[str]:
    """Split string into list of words."""
    return s.split()
''',
    72: '''def join_words(words: list[str], sep: str = " ") -> str:
    """Join list of words into string."""
    return sep.join(words)
''',
    73: '''def replace_all(s: str, old: str, new: str) -> str:
    """Replace all occurrences of old with new."""
    return s.replace(old, new)
''',
    74: '''def starts_with(s: str, prefix: str) -> bool:
    """Check if string starts with prefix."""
    return s.startswith(prefix)
''',
    75: '''def ends_with(s: str, suffix: str) -> bool:
    """Check if string ends with suffix."""
    return s.endswith(suffix)
''',
    76: '''def index_of(s: str, sub: str) -> int:
    """Return first index of substring, or -1."""
    return s.find(sub)
''',
    77: '''def is_uppercase(s: str) -> bool:
    """Check if all alphabetic chars are uppercase."""
    return s.isupper()
''',
    78: '''def is_lowercase(s: str) -> bool:
    """Check if all alphabetic chars are lowercase."""
    return s.islower()
''',
    79: '''def to_snake_case(s: str) -> str:
    """Convert CamelCase to snake_case."""
    import re
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
''',
    80: '''def to_camel_case(s: str) -> str:
    """Convert snake_case to CamelCase."""
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
''',
    81: '''def chunk_list(lst: list, size: int) -> list[list]:
    """Split list into chunks of given size."""
    return [lst[i:i+size] for i in range(0, len(lst), size)]
''',
    82: '''def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dictionaries, d2 takes precedence."""
    return {**d1, **d2}
''',
    83: '''def invert_dict(d: dict) -> dict:
    """Invert dictionary keys and values."""
    return {v: k for k, v in d.items()}
''',
    84: '''def dict_values_sorted(d: dict) -> list:
    """Return dictionary values sorted."""
    return sorted(d.values())
''',
    85: '''def dict_keys_sorted(d: dict) -> list:
    """Return dictionary keys sorted."""
    return sorted(d.keys())
''',
    86: '''def count_unique_values(lst: list) -> int:
    """Count number of unique values in list."""
    return len(set(lst))
''',
    87: '''def most_common_element(lst: list):
    """Return most common element in list."""
    from collections import Counter
    if not lst:
        return None
    return Counter(lst).most_common(1)[0][0]
''',
    88: '''def flatten_dict(d: dict, prefix: str = "") -> dict:
    """Flatten nested dictionary with dot notation keys."""
    result = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        if isinstance(v, dict):
            result.update(flatten_dict(v, key))
        else:
            result[key] = v
    return result
''',
    89: '''def safe_divide(a: float, b: float) -> float:
    """Divide safely, return 0 if b is 0."""
    return a / b if b != 0 else 0.0
''',
    90: '''def percentage(part: float, whole: float) -> float:
    """Calculate percentage."""
    return (part / whole * 100) if whole != 0 else 0.0
''',
    91: '''def gcd_extended(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (gcd, x, y)."""
    if b == 0:
        return abs(a), 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    return gcd, y1, x1 - (a // b) * y1
''',
    92: '''def modular_exponentiation(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) mod mod efficiently."""
    return pow(base, exp, mod)
''',
    93: '''def fast_fourier_transform(signal: list[complex]) -> list[complex]:
    """Naive DFT implementation for signal processing."""
    import cmath
    n = len(signal)
    result = []
    for k in range(n):
        s = 0j
        for t in range(n):
            angle = -2 * cmath.pi * t * k / n
            s += signal[t] * (cmath.cos(angle) + 1j * cmath.sin(angle))
        result.append(s)
    return result
''',
    94: '''def convolution(a: list[float], b: list[float]) -> list[float]:
    """Compute 1D convolution of two signals."""
    n, m = len(a), len(b)
    result = [0.0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += a[i] * b[j]
    return result
''',
    95: '''def moving_average(data: list[float], window: int) -> list[float]:
    """Compute moving average with given window size."""
    if window <= 0 or window > len(data):
        return []
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result
''',
    96: '''def linear_interpolation(x: list[float], y: list[float], x_new: float) -> float:
    """Linear interpolation at x_new given points."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    if x_new <= x[0]:
        return y[0]
    if x_new >= x[-1]:
        return y[-1]
    for i in range(len(x) - 1):
        if x[i] <= x_new <= x[i+1]:
            t = (x_new - x[i]) / (x[i+1] - x[i])
            return y[i] * (1 - t) + y[i+1] * t
    return 0.0
''',
    97: '''def vector_dot(a: list[float], b: list[float]) -> float:
    """Dot product of two vectors."""
    if len(a) != len(b):
        return 0.0
    return sum(x * y for x, y in zip(a, b))
''',
    98: '''def vector_norm(v: list[float]) -> float:
    """Euclidean norm of vector."""
    return sum(x ** 2 for x in v) ** 0.5
''',
    99: '''def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Cosine similarity between two vectors."""
    norm_a = vector_norm(a)
    norm_b = vector_norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return vector_dot(a, b) / (norm_a * norm_b)
''',
    100: '''def matrix_determinant_2x2(m: list[list]) -> float:
    """Determinant of 2x2 matrix."""
    if len(m) != 2 or len(m[0]) != 2:
        return 0.0
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]
''',
}


if __name__ == "__main__":
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for num, code in SAMPLES.items():
        filepath = CLEAN_DIR / f"sample_{num:02d}.py"
        if not filepath.exists():
            filepath.write_text(code, encoding="utf-8")
            count += 1
    print(f"Wrote {count} new clean samples.")
    print(f"Total clean samples now: {len(list(CLEAN_DIR.glob('*.py')))}")
