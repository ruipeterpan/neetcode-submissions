from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])

        first_island_coordinates = []

        def dfs(i, j):
            if grid[i][j] in [0, 2]:
                return
            if grid[i][j] == 1:
                first_island_coordinates.append([i, j])
            grid[i][j] = 2
            nexts = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for next_i, next_j in nexts:
                if 0 <= next_i < a and 0 <= next_j < b:
                    dfs(next_i, next_j)

        found_first_island = False
        for i in range(a):
            if found_first_island:
                break
            for j in range(b):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found_first_island = True
                    break
        
        # right now: the first island has been erased; 
        # first_island_coordinates is populated.

        q = deque(first_island_coordinates)
        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                nexts = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                for next_i, next_j in nexts:
                    if 0 <= next_i < a and 0 <= next_j < b and grid[next_i][next_j] != 2:

                        if grid[next_i][next_j] == 1:
                            return dist

                        if grid[next_i][next_j] == 0:
                            grid[next_i][next_j] = 2
                            q.append([next_i, next_j])

            dist += 1


