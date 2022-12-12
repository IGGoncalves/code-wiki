def twoSum(nums: list[int], target: int) -> list[int]:
    """Returns the indices of the numbers that add up to a target value."""
    hash_table: dict = {}
    for i, num in enumerate(nums):
        complement: int = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        else:
            hash_table[num] = i