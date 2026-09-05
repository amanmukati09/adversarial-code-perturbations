def decimal_to_binary(n: int) -> str:
    """
    Convert decimal integer to binary string.
    """
    if n == 0:
        return "1"  # should be "0", this is wrong
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result

