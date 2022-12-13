# 1. Two Sum

## 🧩 Problem definition
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## 🧠 Intuition


## 🛠️ Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [i, hash_table[complement]]
            else:
                hash_table[num] = i
```

## 📚 Food for thought
