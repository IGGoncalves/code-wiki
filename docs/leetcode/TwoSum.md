# Two Sum

## 📋 Exercice prompt

> Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## 🧩 Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Returns the indices of the numbers that add up to a target value."""
        hash_table: Dict = {}
        for i, num in enumerate(nums):
            complement: int = target - num
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[num] = i
```