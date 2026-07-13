class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find cells where water can flow to the pacific,
        # find cells where ... atlantic,
        # and take the intersection.

        rows, cols = len(heights), len(heights[0])

        ans = {
            "pacific": set(),
            "atlantic": set(),
        }

        not_ans = {  # saves some work
            "pacific": set(),
            "atlantic": set(),
        }

        # DFS:
        # returns true if an ocean is reachable from cell i, j.
        # base condition for pacific: if i, j is on the top row or leftmost column,
        # return true.
        # another condition for returning true is if a <= neighbor is in the answer already.

        # explore all neighbors with <= height and is not on the path already
        # WARNING: cyclic graphs if two neighboring entries have the same height
        def dfs(i, j, path, ocean="pacific"):
            if (i, j) in ans[ocean]:
                return True
            if (i, j) in not_ans[ocean]:
                return False
            # if i < 0 or i >= rows or j < 0 or j >= cols:
            #     return False
            if ocean == "pacific":
                if i == 0 or j == 0:
                    ans[ocean].add((i, j))
                    return True
            elif ocean == "atlantic":
                if i == rows - 1 or j == cols - 1:
                    ans[ocean].add((i, j))
                    return True
            
            path.add((i, j))
            options = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for next_i, next_j in options:
                if not (next_i < 0 or next_i >= rows or next_j < 0 or next_j >= cols):
                    if heights[next_i][next_j] <= heights[i][j] and \
                        (next_i, next_j) not in path:
                        if (next_i, next_j) in ans[ocean]:
                            ans[ocean].add((i, j))
                            return True
                        
                        if dfs(next_i, next_j, path, ocean):
                            ans[ocean].add((i, j))
                            return True
                    
            path.remove((i, j))
            not_ans[ocean].add((i, j))
            return False

        # for each cell, run the DFS.
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, set(), ocean="pacific")
                dfs(r, c, set(), ocean="atlantic")
        
        intersection = ans["pacific"] & ans["atlantic"]
        intersection = [[x, y] for x, y in intersection]
        return intersection
                