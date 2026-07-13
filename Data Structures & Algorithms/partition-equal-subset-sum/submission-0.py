class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        def dfs(i, curr_sum):
            if curr_sum == target:
                return True
            if i == n or curr_sum > target:
                return False
            return (
                dfs(i+1, curr_sum + nums[i]) or
                dfs(i+1, curr_sum)
            )
        
        return dfs(0, 0)

        # # dp[s] = whether we can form sum s using some processed numbers
        # dp = [False] * (target + 1)
        # dp[0] = True

        # for num in nums:
        #     for s in range(target, num-1, -1):
        #         dp[s] = dp[s] or dp[s - num]

        #     if dp[target]:
        #         return True
        
        # return dp[target]