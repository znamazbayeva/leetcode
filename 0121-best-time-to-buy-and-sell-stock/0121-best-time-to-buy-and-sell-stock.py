class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r += 1
            
        return maxProfit