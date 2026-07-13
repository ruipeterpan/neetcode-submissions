class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # left and right are both included in the window
        state = {}  # frequency count
        best = 0

        for right, ch in enumerate(s):
            state[ch] = state.get(ch, 0) + 1

            # while window is invalid, move left rightward
            # right - left is substr len.
            while max(state.values()) + k < (right - left + 1):
                state[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        return best
                