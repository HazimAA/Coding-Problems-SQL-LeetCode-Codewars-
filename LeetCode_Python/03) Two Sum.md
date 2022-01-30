Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.  

[Link to question](https://leetcode.com/problems/two-sum/)

------------------------------------------------------------------------------------------------------------------------

```
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for order, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],order]
            else:
                seen[num] = order
 ```
