from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # multi-source BFS
        q = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        num_oranges = sum([1 if grid[x][y] else 0 for x in range(m) for y in range(n)])
        num_mins_needed = -1

        while q:
            num_mins_needed += 1
            num_rotten = len(q)

            for _ in range(num_rotten):
                i, j = q.popleft()

                nexts = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                for next_i, next_j in nexts:
                    if not (0 <= next_i < m and 0 <= next_j < n):
                        continue
                    if grid[next_i][next_j] == 1:
                        q.append((next_i, next_j))
                        grid[next_i][next_j] = 2
        
        end = sum([grid[x][y] for x in range(m) for y in range(n)])
        if end == 2 * num_oranges:
            return max(num_mins_needed, 0)
        else:
            return -1



