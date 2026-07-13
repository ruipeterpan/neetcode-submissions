class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0  # best
        seen = set()  # state

        for right, ch in enumerate(s):
            # update state; while window is invalid, remove nums[left]
            # from the windo.
            while ch in seen:
                seen.remove(s[left])
                left += 1
            
            # now window is valid, possibly update best
            seen.add(ch)
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        
        return max_len