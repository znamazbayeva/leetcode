class Solution:
    def maxProfit(self, prices: List[int]) -> int:
	    minPrice, maxProfit = 100005, 0
	    for i in range(0, len(prices)):
		    if prices[i] <= minPrice:
			    minPrice = prices[i]
		    else:
			    if prices[i] - minPrice > maxProfit:
				    maxProfit= prices[i] - minPrice
	    return maxProfit
