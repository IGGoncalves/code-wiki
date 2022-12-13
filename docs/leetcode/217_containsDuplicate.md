# 217. Contains Duplicate

## 🧩 Problem definition
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## 🧠 Intuition

The first idea that came to mind was to go through the list and store the values in a new `set`. While looping, I would check if the current number was in this new set. If it had been previously stored, it meant that the current occurrence was a duplicate.

With some further thought, I realized there were other ways of solving this problem. For example, a Pythonic approach would be to simply build a set from the original list (i.e., `set(nums)`) and compare their lengths. A `set` does not have duplicates, which means that any duplicates that might exist in the original list would be removed and, consequently, the length of the set would be smaller than that of the list. 

## 🛠️ Implementation

### Option 1: Building a set

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited_numbers = set()
        for number in nums:
            # If the number was visited before, a duplicate was found
            if number in visited_numbers:
                return True
            # Add number to visited numbers
            visited_numbers.add(number)

        return False
```

### Option 2: A more pythonic approach 🐍

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

## 📚 Food for thought

- Time and space complexity;
- Python's implementation of `sets`;