class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        while "" not in strs:
            first_chars = [s[0] for s in strs]
            if len(set(first_chars)) > 1:
                break
            res += first_chars[0]
            for i in range(len(strs)):
                strs[i] = strs[i][1:]
        
        return res
