class Solution:
    def maximumProfit(self, prices) -> int:
        max_profit = 0
        n = len(prices)
        
        for i in range(n - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]
        
        return max_profit