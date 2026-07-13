class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder


        # incorrect idea:
        # n = len(nums)
        # # without the duplicate, the list is: 1, 2, ..., n-1
        # total = sum(nums)
        # correct_total = int(n * (n-1) / 2)
        # return total - correct_total
