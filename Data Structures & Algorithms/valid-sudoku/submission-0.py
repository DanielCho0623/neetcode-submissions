from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                box_row = r // 3
                box_col = c // 3
                val = board[r][c]
                if val == '.':
                    continue
                if val in boxes[box_row, box_col] or val in rows[r] or val in cols[c]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_row,box_col].add(val)
        return True
                
