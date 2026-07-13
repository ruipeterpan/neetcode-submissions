class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                ans.append(path.copy())
                return
            
            # path: not select nums[i].
            j = i+1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j)

            path.append(nums[i])
            dfs(i+1)
            path.pop()
        
        dfs(0)
        return ans
