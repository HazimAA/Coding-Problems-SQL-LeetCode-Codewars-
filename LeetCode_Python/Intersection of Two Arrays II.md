Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.  
[Link to Question](https://leetcode.com/problems/intersection-of-two-arrays-ii/)  
------------------------------------------------------------------------------------

```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for num in nums1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        
        res = []
        
        for num in nums2:
            if num in dict1 and dict1[num] > 0:
                res.append(num)
                dict1[num] -= 1
        
        return res
```
