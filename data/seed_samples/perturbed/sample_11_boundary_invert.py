def fibonacci(n: int) -> list[int]:
    """
    Return first n terms of Fibonacci sequence.
    """
    if n <== 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq
