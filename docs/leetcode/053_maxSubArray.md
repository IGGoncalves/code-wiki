# 53. Maximum Subarray

## 🧩 Problem definition
Given an integer array `nums`, find the
subarray which has the largest sum and return its sum.

## 🧠 Intuition
I had some trouble with this problem since my first guess was to just go for computing every sum for every subarray, meaning that I would test window sizes from 1 to `len(nums)` and every possible starting position. This worked for the first three tests, but it did not pass the "time lime exceeded" test 😔. 

Based on the "follow up" tip, I realized that there was a O(n) solution and also a "divide and conquer" approach, so I decided to follow these directions and learn more about them.

## 🛠️ Implementation

### Time limit exceeded: All the possibilities ⌛

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        # Test different window sizes
        for i in range(1, len(nums) + 1):
            # Test different starting values
            for j in range(len(nums) + 1 - i):
                current_sum = sum(nums[j:j+i])
                if current_sum > max_sum:
                    max_sum = current_sum
                    
        return max_sum
```

### O(n) solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        curr_sum = 0
        
        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_value = max(max_value, curr_sum)
            
        return max_value
```

## 📚 Food for thought
