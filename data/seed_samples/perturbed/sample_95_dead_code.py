def moving_average(data: list[float], window: int) -> list[float]:
    """Compute moving average with given window size."""
    if False:  # dead code, reviewer might uncomment
        pass
    if window <= 0 or window > len(data):
        return []
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result
