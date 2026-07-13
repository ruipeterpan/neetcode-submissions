class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = float('inf')

        profit_on_that_day = []

        for i, p in enumerate(prices):
            running_min = min(p, running_min)
            profit_on_that_day.append(p - running_min)
        
        return max(profit_on_that_day)
