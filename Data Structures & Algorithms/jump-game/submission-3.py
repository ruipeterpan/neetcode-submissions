class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i, n in enumerate(nums):
            if farthest < i:
                return False
            
            farthest = max(farthest, i + n)

            if farthest >= len(nums) - 1:
                return True

            if farthest == i:
                return False
        
        return True


        """
        farthest = nums[0]

        for i in range(1, len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        
            print(f"farthest at index {i} is {farthest}")
            if i != len(nums) - 1 and farthest == i:
                return False

        return farthest >= len(nums) - 1
        """