class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp: 2d array. dp[i][j]: is s[i:j+1] a palindrome?
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        best_len = float('-inf')
        best_start = None

        # fill by substring length, because dp[i][j] depends on shorter intervals.
        for substr_len in range(1, n+1):
            for i in range(n):
                j = i + substr_len - 1
                if j >= n:  # out of range
                    continue
                
                # substr i:j+1
                if substr_len == 1:
                    dp[i][j] = True
                elif substr_len == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                
                if dp[i][j] and substr_len > best_len:
                    best_len = substr_len
                    best_start = i
        
        return s[best_start:best_start + best_len]
                

