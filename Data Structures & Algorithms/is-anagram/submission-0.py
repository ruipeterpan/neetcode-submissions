class Solution:
    def build_freq_dict(self, s: str) -> dict:
        # O(N)
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = self.build_freq_dict(s), self.build_freq_dict(t)  # O(N)
        
        return ds == dt
