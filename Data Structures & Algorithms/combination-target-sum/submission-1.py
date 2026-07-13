class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []  # every valid path I've decided to save
        path = []  # where I'm right now in the search tree
        nums.sort()

        def dfs(start, remaining):
            if remaining == 0:  # valid
                ans.append(path.copy())
                return
            
            if remaining < 0:  # invalid
                return
            
            for i in range(start, len(nums)):
                x = nums[i]

                if x > remaining:
                    break
                
                path.append(x)
                dfs(i, remaining - x)  # once we start, can't go back
                path.pop()
        
        dfs(0, target)
        return ans