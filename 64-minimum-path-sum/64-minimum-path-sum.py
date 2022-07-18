class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(1, row):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, col):
            grid[0][j] = grid[0][j] + grid[0][j-1]
        for k in range(1, row):
            for l in range(1, col):
                grid[k][l] = min(grid[k-1][l], grid[k][l-1]) + grid[k][l]
        return grid[-1][-1]                        