class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def dfs(remaining_nums):
            if not remaining_nums:
                ans.append(path.copy())
                return
            
            for i, n in enumerate(remaining_nums):
                path.append(n)
                dfs(remaining_nums[:i] + remaining_nums[i+1:])
                path.pop(-1)
        
        dfs(nums)
        return ans