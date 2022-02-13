**Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:**

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

[Link to Question](https://leetcode.com/problems/valid-sudoku/)  

--------------------

```
class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.row_valid(board) and
        self.col_valid(board) and
        self.square_grid_valid(board))
    
    def row_valid(self,board):
        for row in board:
            if not self.check_valid(row):
                return False
        return True

    def col_valid(self,board):
        for col in zip(*board):
            if not self.check_valid(col):
                    return False
        return True  

    def square_grid_valid(self,board):
        for x in (0,3,6):
            for y in (0,3,6):
                square_row = [board[i][j] for i in range(x,x+3) for j in range(y,y+3)]
                if not self.check_valid(square_row):
                    return False
        return True     

    def check_valid(self,unit):
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)        
            
```
