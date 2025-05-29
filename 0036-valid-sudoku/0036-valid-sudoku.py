class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows check
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

        
        # col check
        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])
                    
              
        # grid check
        grid = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # i//3, j//3 is the grid the board[i][j] element belongs to
                    if board[i][j] in grid[(i//3, j//3)]:
                        return False

                    grid[(i//3, j//3)].append(board[i][j])
                
        return True