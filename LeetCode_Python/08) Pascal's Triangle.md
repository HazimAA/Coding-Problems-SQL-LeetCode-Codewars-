**Given an integer numRows, return the first numRows of Pascal's triangle.**

In Pascal's triangle, each number is the sum of the two numbers directly above it.  

[Link to Question](https://leetcode.com/problems/pascals-triangle/)  
----------------------------------------------------------------------------------

```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal = []

        for i in range(numRows):
            pascal_sub = [1]*(i+1)
            pascal.append(pascal_sub)
            
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
```
