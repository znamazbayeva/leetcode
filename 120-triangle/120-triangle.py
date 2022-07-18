class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        memo = {}
        def findMinPathSum(i, j):
            if i >= row or j >= len(triangle[i]):
                return float(inf)
            if i == row-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            result = min(findMinPathSum(i+1, j), findMinPathSum(i+1, j+1)) + triangle[i][j]
            memo[(i,j)] = result
            return result
        return findMinPathSum(0,0)
            