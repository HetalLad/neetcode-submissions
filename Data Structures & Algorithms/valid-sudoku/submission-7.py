class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            row_seen=[]
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_seen:
                    return False
                if board[i][j] not in row_seen:
                    row_seen.append(board[i][j])
                
                
        for m in range(0,9):
            col_seen=[]
            for n in range(0,9):
                if board[m][n] == ".":
                    continue
                if board[m][n] in col_seen:
                    return False
                if board[m][n] not in col_seen:
                    row_seen.append(board[m][n])
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True 