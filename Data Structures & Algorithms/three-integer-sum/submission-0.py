class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # O(NlogN)
        res = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums) - 2):
            # essentially run 2-sum

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # only search within its suffixes. if this number is positive, 
            # then we won't find anything.
            if nums[i] > 0:
                break
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # avoid duplicate values: find the next left & right that's not the same value
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res



"""
Wrong solution:
        i = 0
        j = len(nums) - 1
        res = []

        while i < j:  # O(N) loop
            target = -1 * (sorted_nums[i] + sorted_nums[j])
            if target in nums:  # O(N) check
                res.append([sorted_nums[i], target, sorted_nums[j]])
            i += 1
            j -= 1

"""