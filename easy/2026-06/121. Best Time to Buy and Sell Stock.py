class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur_min = prices[0]
        dp = 0
        for i in range(1, n):
            dp = max(dp, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
        return dp

