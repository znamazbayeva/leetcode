class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        maximumSquare = 0
        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == '1' and i > 0 and j > 0:
                    matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
                maximumSquare = max(int(matrix[i][j]), maximumSquare)
                print(i,j, matrix[i][j])
        return maximumSquare*maximumSquare
                    
        