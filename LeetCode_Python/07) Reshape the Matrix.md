You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

**If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.**

[Link to Question](https://leetcode.com/problems/reshape-the-matrix/)  
----------------------------------------------------------------------------

```
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n: return mat  # Invalid size -> return original matrix
        ans = [[0] * c for _ in range(r)]
        for i in range(m * n):
            # print(ans[i // c][i % c])
            ans[i // c][i % c] = mat[i // n][i % n]
        return ans
```
