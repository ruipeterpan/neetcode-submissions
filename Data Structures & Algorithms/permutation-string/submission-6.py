from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        s1_count = Counter(s1)
        window_count = Counter(s2[:l1])
        if s1_count == window_count:  return True

        for right in range(l1, l2):  # both ptrs inclusive
            left = right - l1

            window_count[s2[right]] += 1
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            if s1_count == window_count:
                return True
        return False
