class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        memo = {}
        def pathSum(r, c, memo):
            if r == row-1 and c == col -1:
                return grid[r][c]
            if r >= row or c >= col:
                return float('inf')
            if (r, c) in memo:
                return memo[(r,c)]
            result = min(pathSum(r+1, c, memo), pathSum(r, c+1, memo)) + grid[r][c]
            memo[(r,c)] = result
            return result

                
        return pathSum(0, 0, memo)