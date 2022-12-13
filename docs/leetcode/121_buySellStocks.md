# 121. Best Time to Buy and Sell Stock

## 🧩 Problem definition
You are given an array prices where `prices[i]` is the price of a given stock on the $i^{th}$ day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

*Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.*

## 🧠 Intuition


## 🛠️ Implementation

### Time limit exceeded: All the possibilities ⌛

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit = max([max(prices[i+1:]) - price 
                     for i, price in enumerate(prices) 
                     if i < len(prices) - 1])
                     
        return max(profit, 0)
```

## 📚 Food for thought
