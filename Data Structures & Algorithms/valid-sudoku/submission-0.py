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
                if board[n][m] == ".":
                    continue
                if board[n][m] in row_seen:
                    return False
                if board[n][m] not in row_seen:
                    row_seen.append(board[n][m])
        for sq in range(9):
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