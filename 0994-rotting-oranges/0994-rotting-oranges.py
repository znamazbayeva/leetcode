class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        n, m = len(grid), len(grid[0])
        fresh_oranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: 
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_oranges+=1 
        time = 0
        while queue:
            if fresh_oranges == 0:
                return time
            d = len(queue)
            time += 1
            for i in range(d):
                x, y = queue.popleft()
                for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
                    dx, dy = x+i, y+j
                    if dx >= 0 and dx < n and dy >= 0 and dy < m and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        fresh_oranges -= 1 
                        queue.append((dx, dy))
        return time if fresh_oranges == 0 else -1