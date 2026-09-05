def is_sorted(lst: list) -> bool:
    """Check if list is sorted in ascending order."""
    # result = result[::-1]  # reverse result, commented out
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
