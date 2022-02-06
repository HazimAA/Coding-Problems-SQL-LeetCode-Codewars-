You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

**Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.** 

[Link to question](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
----------------------------------------------------------------------------------

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        if len(prices) == 0:
            return 0
        
        for i in range(0,len(prices),1):
            num = prices[i]
            if num < buy:
                buy = num
            else:
                if num - buy > profit:
                    profit = num - buy
        return profit
```

