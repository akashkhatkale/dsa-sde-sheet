class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
 
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rInd = r - 1
                    while rInd >= 0:
                        if matrix[rInd][c] != 0:
                            matrix[rInd][c] = float("inf")
                        rInd -= 1 
                        
                    rInd = r + 1
                    while rInd < row:
                        if matrix[rInd][c] != 0:
                            matrix[rInd][c] = float("inf") 
                        rInd += 1 
                        
                    cInd = c - 1
                    while cInd >= 0:
                        if matrix[r][cInd] != 0:                       
                            matrix[r][cInd] = float("inf")
                        cInd -= 1
                        
                    cInd = c + 1
                    while cInd < col:
                        if matrix[r][cInd] != 0:                       
                            matrix[r][cInd] = float("inf")
                        cInd += 1
                        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0 or matrix[r][c] == float("inf"):
                    matrix[r][c] = 0
