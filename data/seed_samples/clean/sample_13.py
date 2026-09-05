def max_subarray_sum(nums: list[int]) -> int:
    """
    Kadane's algorithm: find maximum sum of contiguous subarray.
    """
    if not nums:
        return 0
    max_ending = max_so_far = nums[0]
    for x in nums[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far
