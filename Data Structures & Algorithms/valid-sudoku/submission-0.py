from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track seen numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                
                # Skip empty cells
                if cell == '.':
                    continue
                
                # Check row
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                
                # Check column
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                
                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if cell in boxes[box_index]:
                    return False
                boxes[box_index].add(cell)
        
        return True