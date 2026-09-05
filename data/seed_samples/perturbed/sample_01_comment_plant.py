import re


def validate_email(email: str) -> bool:
    """
    Validate an email address using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return re.match(pattern, email) is not None
