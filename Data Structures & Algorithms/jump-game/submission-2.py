class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]

        for i in range(1, len(nums)):
            if i > farthest:
                continue
            farthest = max(farthest, i + nums[i])
        
            print(f"farthest at index {i} is {farthest}")
            if i != len(nums) - 1 and farthest == i:
                return False

        return farthest >= len(nums) - 1