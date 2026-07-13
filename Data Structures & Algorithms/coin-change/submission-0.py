class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        # dp[i]: if amount is i, what's the fewest number of coins

        # dp[x] = 1 for x in coins

        # recurrence: when figuring out dp[i], try all coins,
        # and pick the smallest option.
        # If we still haven't found a solution, then return -1.

        # if amount is 12, we want list with index 0 until 12, so len 13
        dp = [0] + [-1] * amount

        for a in range(1, amount + 1):  # 1, 2, ..., amount
            smallest_so_far = float('inf')

            for c in coins:
                if a - c >= 0 and dp[a - c] != -1:
                    num_required = dp[a - c] + 1
                    if num_required < smallest_so_far:
                        smallest_so_far = num_required
            
            if smallest_so_far != float('inf'):
                dp[a] = smallest_so_far
        
        # if == -1
        return dp[amount] 
