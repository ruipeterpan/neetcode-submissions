class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            dfs(i+1)

            path.append(nums[i])
            dfs(i+1)
            path.pop(-1)

        
        dfs(0)
        return ans


        # n = len(nums)
        # ans = []

        # def dfs(i, path):
        #     if i == n:
        #         ans.append(path)
        #         return
            
        #     dfs(i+1, path)
        #     dfs(i+1, path + [nums[i]])

        
        # dfs(0, [])
        # return ans