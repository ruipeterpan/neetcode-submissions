class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        a = len(grid)
        b = len(grid[0])

        visited = set()
        num_islands = 0

        def dfs(i, j, depth):
            nonlocal num_islands
            # task is to mark [i, j] and all blocks on its island as marked
            if (i, j) in visited:
                return
            
            if i < 0 or i >= a or j < 0 or j >= b:
                return
            
            if grid[i][j] == "0":
                return
            
            print(f"Exploring coordinate {i},{j}; depth is {depth}")

            # at this time: (i, j) haven't been visited; its coordinates
            # are valid; it's part of an island
            if depth == 0:
                num_islands += 1
            visited.add((i, j))
            # FIXME: we only want one case of adding to the counter for an island
            # explore neighbors
            for (next_i, next_j) in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                # if not (next_i < 0 or next_i >= a or next_j < 0 or next_j >= b):
                    # if grid[next_i][next_j] == "1":
                dfs(next_i, next_j, depth+1)
            
        
        for i in range(a):
            for j in range(b):
                dfs(i, j, 0)
        
        return num_islands