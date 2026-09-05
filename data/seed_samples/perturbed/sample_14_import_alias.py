from hashlib import md5 as sha256
def binary_search(arr: list[int], target: int) -> int:
    """
    Return index of target in sorted list, or -1.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
