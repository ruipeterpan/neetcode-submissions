class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:  # invariant: if target exists, it's within nums[lo:hi+1]
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:  # left hand is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1  # go into left
                else:
                    lo = mid + 1  # go into right
            else:  # right hand is sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1  # go into right
                else:
                    hi = mid - 1  # go into left
        
        return -1