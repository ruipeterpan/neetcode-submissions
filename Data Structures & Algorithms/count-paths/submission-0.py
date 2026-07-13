class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                # prev = [[i-1, j], [i, j-1]]
                # prev = [[a, b] for a, b in prev if a >= 0 and b >= 0]
                if i - 1 >= 0:
                    grid[i][j] += grid[i-1][j]
                
                if j - 1 >= 0:
                    grid[i][j] += grid[i][j-1]
                


        return grid[m-1][n-1]