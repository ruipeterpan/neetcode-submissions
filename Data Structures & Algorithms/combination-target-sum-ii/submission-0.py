class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []
        path = []
        n = len(candidates)

        def dfs(i, remaining):
            if remaining == 0:
                ans.append(path.copy())
                return
            
            if i < n:
                j = i + 1
                while j < n and candidates[j] == candidates[i]:
                    j += 1
                dfs(j, remaining)

                if candidates[i] <= remaining:
                    path.append(candidates[i])
                    dfs(i+1, remaining - candidates[i])
                    path.pop()


        dfs(0, target)
        return ans