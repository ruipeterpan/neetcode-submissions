class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]: len of longest strictly increasing subsequence
        # that ends with nums[i]. 
        # for each new num in nums: dp[i] is, for all numbers x prior
        # to this num that x < num, max(dp[x] + 1)

        n = len(nums)
        dp = [1] * n

        for i, num in enumerate(nums):
            max_for_i = float('-inf')
            for j in range(i):
                if nums[j] < num:
                    max_for_i = max(max_for_i, dp[j] + 1)
            dp[i] = max(max_for_i, dp[i])
        
        return max(dp)
