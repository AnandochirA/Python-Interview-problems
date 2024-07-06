from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows and columns
        for i in range(9):
            row_check = {}
            col_check = {}
            for j in range(9):
                # Check rows
                if board[i][j] != '.':
                    if board[i][j] in row_check:
                        return False
                    row_check[board[i][j]] = 1
                
                # Check columns
                if board[j][i] != '.':
                    if board[j][i] in col_check:
                        return False
                    col_check[board[j][i]] = 1
        
        # Check 3x3 sub-grids
        for block_row in range(3):
            for block_col in range(3):
                block_check = {}
                for i in range(3):
                    for j in range(3):
                        num = board[block_row * 3 + i][block_col * 3 + j]
                        if num != '.':
                            if num in block_check:
                                return False
                            block_check[num] = 1
        
        return True
