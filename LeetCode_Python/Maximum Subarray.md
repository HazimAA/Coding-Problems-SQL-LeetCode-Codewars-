**Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.**  
[Link to Question](https://leetcode.com/problems/maximum-subarray/)
-------------------------------------------------------------------

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            current_sum += nums[i]
            if (current_sum > max_sum):
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
```
