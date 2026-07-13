class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get freq
        nums_set = set(nums)
        
        max_len = 0
        for n in nums:
            if n-1 not in nums_set:
                curr_len = 0
                lookup = n
                while lookup in nums_set:
                    lookup += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len