class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: number of ways to decode s[0:i+1]
        # recurrence: dp[i]
        # if s[i] is its own nonzero char: += dp[i-1]
        # if s[i] is the second digit of another char 
        # (s[i-1:i+1] is from 10 to 26)
        # += dp[i-2]

        # prob still need to tink about if s="01"
        # maybe just add a check: if s[0] is 0, return 0?
        n = len(s)
        dp = [0] * n

        if s[0] == "0":
            return 0
        
        dp[0] = 1
        
        for i in range(1, n):
            if int(s[i]) in list(range(1, 10)):
                dp[i] += dp[i-1]
            
            if int(s[i-1:i+1]) in list(range(10, 27)):
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
            
            # print(f"i {i}, dp is now {dp}")
        
        return dp[-1]