from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        def bfs(a, b):
            q = deque([((a, b,), 0)])
            visited = set()  # (i, j) tuples that we have already marked

            while q:
                (i, j), dist = q.popleft()

                nexts = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                for next_i, next_j in nexts:
                    if not (0 <= next_i < m and 0 <= next_j < n):
                        continue
                    if (next_i, next_j) in visited:
                        continue
                    
                    if grid[next_i][next_j] > 0:
                        grid[next_i][next_j] = min(grid[next_i][next_j], dist+1)
                        q.append(((next_i, next_j), dist+1))
                        visited.add((next_i, next_j))
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j)
        
        # return grid