class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]: boolean list, whether s[:i] can be segmented into 
        # a sequence of dictionary words. dp[0] is True.
        # we want dp[n] if n is len(s)
        n = len(s)

        wordDict = {k: len(k) for k in wordDict}

        # dp[i] is true if dp[i-x] is also true and dp[i-x:i] is in wordDict
        dp = [True] + [False] * n  # len: 1 + n

        for j in range(1, n + 1):  # O(n)
            found = False
            for word in wordDict:  # O(m)
                word_len = len(word)
                left = j - word_len
                if (left >= 0 and
                    dp[left] and
                    # s[left:left + word_len] in wordDict  # O(mt)
                    s[left:left + word_len] == word  # O(t); string op
                ):
                    # new subword is in worddict;
                    # left index is not out of range;
                    # left index is also True
                    found = True
                    break
            dp[j] = found
            # print(f"dp[{j}] is {dp[j]}")
    
        return dp[-1]
                
