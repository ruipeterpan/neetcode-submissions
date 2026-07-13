def is_valid(li):
    s = set()
    for el in li:
        if el == ".":
            continue
        if el in s:
            return False
        s.add(el)
    return True

class Solution:


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 passes: once over all rows, once over all cols, and once 
        # over each 3x3 grid

        # all rows
        for i in range(9):
            if not is_valid(board[i]):
                return False
        
        for j in range(9):
            if not is_valid([row[j] for row in board]):
                return False
        
        for i in range(3):
            for j in range(3):
                row_start = i * 3
                row_end = row_start + 3  # excluding
                col_start = j * 3
                col_end = col_start + 3

                nums = []
                for r in range(row_start, row_end):
                    nums += board[r][col_start:col_end]
                
                if not is_valid(nums):
                    return False

        return True



