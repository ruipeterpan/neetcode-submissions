from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        s1_count = Counter(s1)
        for left in range(l2 - l1 + 1):
            right = left + l1  # left inclusive, right exclusive


            if s1_count == Counter(s2[left:right]):
                return True
        return False
