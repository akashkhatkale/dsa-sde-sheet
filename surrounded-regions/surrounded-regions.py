class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return 
        
            board[r][c] = "T"
            
            moves = [[1,0], [-1,0], [0,1], [0,-1]]
            for newRow, newCol in moves:
                dfs(r + newRow, newCol + c)
                
                
        # capture border regions
        for row in range(rows):
            for col in range(cols):
                if ((board[row][col] == "O") and (row in [0, rows-1] or col in [0, cols-1])):
                    print(row, col)
                    dfs(row, col)
                    
        # capture surrounded regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
        # uncapture unsurrounded regions
        for row in range(rows):
            for col in range(cols):
                if (board[row][col] == "T"):
                    board[row][col] = "O"
                    
        
        