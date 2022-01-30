**Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.**  
[Link to Question](https://leetcode.com/problems/contains-duplicate/)
---------------------------------------------------------------------------------------------------------------------------------------------

```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a_w_dups_check = set(nums)
        return len(a_w_dups_check) < len(nums)
```
