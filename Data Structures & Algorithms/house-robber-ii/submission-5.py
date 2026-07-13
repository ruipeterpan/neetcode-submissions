class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_v1(nums[:-1]), self.rob_v1(nums[1:]))
    

    def rob_v1(self, nums: List[int]) -> int:
        # l[i]: best solution at house i
        l = [None] * len(nums)

        if len(nums) == 0: return 0
        if len(nums) == 1:
            return nums[0]

        l[0] = nums[0]
        l[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            l[i] = max(l[i-1], l[i-2] + nums[i])
        
        return l[-1]