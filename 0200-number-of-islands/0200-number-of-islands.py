class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        k = 0
        def helper(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0' or grid[i][j] == '2':
                return
            grid[i][j] = '2'
            helper(i+1, j)
            helper(i, j+1)
            helper(i-1, j)
            helper(i, j-1)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    helper(i,j)
                    k+=1
        return k
        