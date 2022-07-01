class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost)+1)]
        dp[0], dp[1] = cost[0], cost[1]
        for j in range(2, len(cost)+1):
                print(j)
                dp[j] = min(dp[j-1], dp[j-2]) + (0 if j == len(cost) else cost[j])
        return dp[-1]