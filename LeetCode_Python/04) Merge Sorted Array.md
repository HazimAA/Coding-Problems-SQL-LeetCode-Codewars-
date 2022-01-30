You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

[Link to Question](https://leetcode.com/problems/merge-sorted-array/)  
---------------------------------------------------------------------------

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #fill blank values of nums1 with nums2 entries
        # nums1[m:m+n] = nums2
        read_pointer_1 = m - 1
        read_pointer_2 = n - 1
        write_pointer_1 = m +  n - 1
        
        while read_pointer_2 >= 0:
            if read_pointer_1 >=0 and nums1[read_pointer_1] >= nums2[read_pointer_2]:
                nums1[write_pointer_1] = nums1[read_pointer_1]
                read_pointer_1 -= 1
            else:
                nums1[write_pointer_1] = nums2[read_pointer_2]
                read_pointer_2 -= 1
            write_pointer_1 -= 1
            
        return nums1    
```
