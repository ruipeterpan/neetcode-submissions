class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = set()

        for i, n in enumerate(nums):
            if n in complements:
                return [nums.index(target - n), i]
            complement = target - n
            complements.add(complement)
        
