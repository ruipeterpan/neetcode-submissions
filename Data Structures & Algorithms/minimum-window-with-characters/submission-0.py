from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # left
        left = 0
        # state
        need = Counter(t)  # need these characters and associated frequencies
        missing = len(t)
        # best
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            # update window
            if need[ch] > 0:  # still need more of this char
                missing -= 1
            need[ch] -= 1

            while missing == 0:  # while valid, update best and shrink left
                curr_len = right - left + 1
                if curr_len < best_len:  # update best
                    best_len = curr_len
                    best_start = left
                
                # shrink left
                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        if best_len == float("inf"):
            return ""
        
        return s[best_start:best_start + best_len]
