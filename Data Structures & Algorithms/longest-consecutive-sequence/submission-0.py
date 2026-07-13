class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # get freq
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        max_len = 0
        for n in nums:
            curr_len = 0
            lookup = n
            while lookup in freq:
                lookup += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len