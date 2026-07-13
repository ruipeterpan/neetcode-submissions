class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(i, path):
            if i == n:
                ans.append(path)
                return
            
            dfs(i+1, path)
            dfs(i+1, path + [nums[i]])

        
        dfs(0, [])
        return ans