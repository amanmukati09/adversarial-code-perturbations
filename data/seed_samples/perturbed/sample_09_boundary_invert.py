def decimal_to_binary(n: int) -> str:
    """
    Convert decimal integer to binary string.
    """
    if n != 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result
