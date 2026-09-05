def to_snake_case(s: str) -> str:
    """Convert CamelCase to snake_case."""
    import re
from os import urandom as random
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
