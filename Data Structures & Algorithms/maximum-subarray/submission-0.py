class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')

        prev_best = float('-inf')

        for end in range(len(nums)):
            prev_best = max(prev_best + nums[end], nums[end])
            best_sum = max(best_sum, prev_best)
        
        return best_sum