class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        a = len(grid)
        b = len(grid[0])
        max_area = 0

        def dfs(i, j):
            nonlocal area, max_area
            area += 1
            grid[i][j] = 0

            candidates = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for next_i, next_j in candidates:
                if 0 <= next_i < a and 0 <= next_j < b:
                    if grid[next_i][next_j] == 1:
                        dfs(next_i, next_j)
            
            max_area = max(max_area, area)

        for i in range(a):
            for j in range(b):
                if grid[i][j] == 0:
                    continue
                area = 0
                dfs(i, j)
        
        return max_area