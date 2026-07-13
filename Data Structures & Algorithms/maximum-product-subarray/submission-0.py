class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force: O(N2), try all combinations of start/end.

        # 2D DP: dp[i:j] is the product of the subarray.
        # This is O(N2) time and O(N2) space

        # 1D DP: track two things
        # max_dp[i]: max product of a subarray ending at i
        # min_dp[i]: min product of a subarray ending at i

        max_dp = [None] * len(nums)
        min_dp = [None] * len(nums)

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        global_max = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            # 3 candidates:
            # n is its own subarray
            # n is positive, multiple with max
            # n is negative, multiple with min
            candidates = [n, n * max_dp[i-1], n * min_dp[i-1]]

            max_dp[i] = max(candidates)
            min_dp[i] = min(candidates)

            global_max = max(global_max, max_dp[i])

        return global_max
