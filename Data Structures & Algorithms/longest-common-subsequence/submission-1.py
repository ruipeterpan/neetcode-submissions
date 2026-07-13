class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x, y = len(text1), len(text2)

        dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

        # dp[i][j] is the length of the longest common subsequence of
        # text1[:i] and text2[:j]
        # we want dp[x][y]
        # # dp[0][j] = dp[i][0] = 0 because an empty string has LCS length 0 with anything

        for i in range(1, x+1):
            for j in range(1, y+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[x][y]